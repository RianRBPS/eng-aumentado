import json
import hashlib
import logging
from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, validator, ValidationError
from sqlalchemy import create_engine, text

# Configuração
DATABASE_URL = "postgresql://postgres:postgres@db:5432/hemodb"
engine = create_engine(DATABASE_URL)

logging.basicConfig(
    level=logging.INFO,
    filename="etl.log",
    format="%(asctime)s %(levelname)s %(message)s"
)

class Hemogram(BaseModel):
    sample_id: str
    patient_id: Optional[str]
    collected_at: datetime
    age: Optional[int]
    sex: Optional[str]
    hemoglobin: Optional[float]
    hematocrit: Optional[float]
    wbc: Optional[float]
    neutrophils_abs: Optional[float]
    lymphocytes_abs: Optional[float]
    platelets: Optional[int]
    municipality_code: Optional[str]

    @validator('sex')
    def sex_values(cls, v):
        if v is None: return v
        v = v.upper()
        if v not in ('M','F','O','U'):
            raise ValueError('invalid sex')
        return v

    @validator('age')
    def age_ok(cls, v):
        if v is None: return v
        if not (0 <= v <= 130):
            raise ValueError('age out of range')
        return v

    @validator('hemoglobin')
    def hb_range(cls, v):
        if v is None: return v
        if not (2.0 <= v <= 25.0):
            raise ValueError('hb out of range')
        return v

    @validator('platelets')
    def plts_range(cls, v):
        if v is None: return v
        if not (1000 <= v <= 5000000):
            raise ValueError('platelets out of range')
        return v

def hash_patient(pid: Optional[str]) -> Optional[str]:
    if not pid: return None
    return hashlib.sha256(pid.encode('utf-8')).hexdigest()

def upsert_row(conn, data: Dict[str, Any]):
    stmt = """
    INSERT INTO hemogram (sample_id, patient_hash, collected_at, age, sex,
                          hemoglobin, hematocrit, wbc, neutrophils_abs,
                          lymphocytes_abs, platelets, municipality_code, raw)
    VALUES (:sample_id, :patient_hash, :collected_at, :age, :sex,
            :hemoglobin, :hematocrit, :wbc, :neutrophils_abs,
            :lymphocytes_abs, :platelets, :municipality_code, :raw)
    ON CONFLICT (sample_id) DO UPDATE
      SET updated_at = now(),
          hemoglobin = EXCLUDED.hemoglobin,
          hematocrit = EXCLUDED.hematocrit,
          wbc = EXCLUDED.wbc,
          platelets = EXCLUDED.platelets;
    """
    conn.execute(text(stmt), **data)

def process_file(path):
    errors = []
    accepted = 0
    with engine.begin() as conn:
        with open(path, 'r', encoding='utf8') as fh:
            for line_no, line in enumerate(fh, start=1):
                try:
                    rec = json.loads(line)
                    payload = {
                        "sample_id": rec.get("id") or rec.get("sample_id"),
                        "patient_id": rec.get("subject", {}).get("reference"),
                        "collected_at": rec.get("effectiveDateTime"),
                        "age": rec.get("age"),
                        "sex": rec.get("sex"),
                        "hemoglobin": rec.get("hb"),
                        "hematocrit": rec.get("ht"),
                        "wbc": rec.get("wbc"),
                        "neutrophils_abs": rec.get("neutrophils_abs"),
                        "lymphocytes_abs": rec.get("lymphocytes_abs"),
                        "platelets": rec.get("platelets"),
                        "municipality_code": rec.get("municipality_code"),
                        "raw": json.dumps(rec)
                    }
                    h = Hemogram(**payload)
                    payload["patient_hash"] = hash_patient(payload["patient_id"])
                    payload["collected_at"] = h.collected_at.isoformat()
                    upsert_row(conn, payload)
                    accepted += 1
                except ValidationError as ve:
                    logging.warning(f"validation error at line {line_no}: {ve.json()}")
                    errors.append({"line": line_no, "error": ve.errors(), "raw": line})
                except Exception as e:
                    logging.exception(f"unexpected error at line {line_no}: {e}")
                    errors.append({"line": line_no, "error": str(e), "raw": line})
    logging.info(f"Processed {path}: accepted={accepted} errors={len(errors)}")
    if errors:
        with open(path + ".deadletter.json", 'w', encoding='utf8') as fh:
            json.dump(errors, fh, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    import sys
    process_file(sys.argv[1])
