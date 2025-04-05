-- migrations/20250404130000_create_site_checks.sql

CREATE TABLE site_checks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    site_url TEXT NOT NULL,
    status_code INTEGER,
    success BOOLEAN NOT NULL,
    response_time_ms INTEGER,
    checked_at TIMESTAMPTZ DEFAULT now()
);
