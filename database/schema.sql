CREATE TABLE user_queries (
    id INTEGER PRIMARY KEY,
    query TEXT
);

CREATE TABLE agent_outputs (
    id INTEGER PRIMARY KEY,
    agent_name TEXT,
    output TEXT
);
