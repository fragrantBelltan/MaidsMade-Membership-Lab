-- Generic public schema example.
-- This is intentionally simplified and is not a production schema.

CREATE TABLE memories (
    id TEXT PRIMARY KEY,
    individual_id TEXT NOT NULL,
    occurred_at TEXT NOT NULL,
    kind TEXT NOT NULL,
    text TEXT NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE decisions (
    id TEXT PRIMARY KEY,
    individual_id TEXT NOT NULL,
    decided_at TEXT NOT NULL,
    choice TEXT NOT NULL,
    reason TEXT,
    evidence_memory_ids TEXT,
    state_before TEXT,
    state_after TEXT
);

-- Concept:
-- memories  = what actually happened
-- decisions = what the individual decided from available evidence and state
