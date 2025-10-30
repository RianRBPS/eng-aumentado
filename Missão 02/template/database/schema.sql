-- schema definitivo: hemogram + alerts + dead_letter

CREATE TABLE IF NOT EXISTS hemogram (
  id BIGSERIAL PRIMARY KEY,
  sample_id TEXT NOT NULL UNIQUE,
  patient_hash TEXT,
  collected_at TIMESTAMP WITH TIME ZONE NOT NULL,
  received_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  age SMALLINT,
  sex VARCHAR(1),
  municipality_code VARCHAR(10),
  hemoglobin NUMERIC(5,2),
  hematocrit NUMERIC(5,2),
  rbc NUMERIC(8,4),
  mch NUMERIC(6,2),
  mchc NUMERIC(6,2),
  mcv NUMERIC(6,2),
  wbc NUMERIC(8,2),
  neutrophils_abs NUMERIC(8,2),
  lymphocytes_abs NUMERIC(8,2),
  monocytes_abs NUMERIC(8,2),
  eosinophils_abs NUMERIC(8,2),
  basophils_abs NUMERIC(8,2),
  platelets INTEGER,
  platelets_mean_volume NUMERIC(6,2),
  flags JSONB,
  raw JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_hemogram_collected_at ON hemogram (collected_at);
CREATE INDEX IF NOT EXISTS idx_hemogram_municipality_collected_at ON hemogram (municipality_code, collected_at);
CREATE INDEX IF NOT EXISTS idx_hemogram_platelets ON hemogram (platelets);
CREATE INDEX IF NOT EXISTS idx_hemogram_hemoglobin ON hemogram (hemoglobin);

CREATE TABLE IF NOT EXISTS alert (
  id BIGSERIAL PRIMARY KEY,
  alert_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  condition TEXT NOT NULL,
  severity SMALLINT NOT NULL,
  sample_id TEXT,
  patient_hash TEXT,
  municipality_code VARCHAR(10),
  payload JSONB,
  acknowledged BOOLEAN DEFAULT FALSE,
  resolved_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX IF NOT EXISTS idx_alert_municipality ON alert (municipality_code);
CREATE INDEX IF NOT EXISTS idx_alert_severity ON alert (severity);

CREATE TABLE IF NOT EXISTS dead_letter (
  id BIGSERIAL PRIMARY KEY,
  source_file TEXT,
  line_no INTEGER,
  error TEXT,
  raw JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);
