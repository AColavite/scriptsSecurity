CREATE TABLE sites (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid,
    url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);