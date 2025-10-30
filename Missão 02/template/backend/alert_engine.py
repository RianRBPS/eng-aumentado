import hashlib, json
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:postgres@db:5432/hemodb"
engine = create_engine(DATABASE_URL)

def make_alert_key(condition, sample_id):
    return hashlib.sha1(f"{condition}|{sample_id}".encode()).hexdigest()

def insert_alert(conn, condition, severity, sample_id, patient_hash, municipality_code, payload):
    key = make_alert_key(condition, sample_id)
    q = """
    INSERT INTO alert (alert_at, condition, severity, sample_id, patient_hash, municipality_code, payload)
    SELECT now(), :condition, :severity, :sample_id, :patient_hash, :municipality_code, :payload
    WHERE NOT EXISTS (
      SELECT 1 FROM alert WHERE payload->>'alert_key' = :key
    )
    """
    payload["alert_key"] = key
    conn.execute(
        text(q),
        dict(
            condition=condition,
            severity=severity,
            sample_id=sample_id,
            patient_hash=patient_hash,
            municipality_code=municipality_code,
            payload=json.dumps(payload),
            key=key
        )
    )

def process_alerts():
    with engine.begin() as conn:
        rows = conn.execute(
            text("SELECT * FROM hemogram WHERE created_at >= now() - interval '1 day'")
        ).fetchall()
        for r in rows:
            if r.platelets and r.platelets < 50000:
                insert_alert(conn, "platelets_lt_50k", 3, r.sample_id, r.patient_hash, r.municipality_code,
                             {"platelets": r.platelets})
            elif r.platelets and r.platelets < 100000:
                insert_alert(conn, "platelets_lt_100k", 2, r.sample_id, r.patient_hash, r.municipality_code,
                             {"platelets": r.platelets})
            if r.hemoglobin and r.hemoglobin < 8:
                insert_alert(conn, "hb_lt_8", 3, r.sample_id, r.patient_hash, r.municipality_code,
                             {"hemoglobin": r.hemoglobin})

if __name__ == "__main__":
    process_alerts()
