-- DDL Script to create destination schema and table
CREATE SCHEMA IF NOT EXISTS etl_demo;

CREATE TABLE IF NOT EXISTS dim_users (
    user_id UUID PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    signup_date TIMESTAMP NOT NULL,
    country VARCHAR(100) NOT NULL,
    is_recent_signup BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);