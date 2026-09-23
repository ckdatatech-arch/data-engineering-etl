# Data Engineering ETL Pipeline Blueprint

A professional, modular Data Engineering ETL pipeline designed in Visual Studio Code. This project generates synthetic user data using **Faker**, cleans and transforms the dataset using **Pandas**, and loads the output into a **PostgreSQL** database running inside a **Docker** container.

---

# How to run the files 

1. Clone to Repo
2. Make sure docker is installed on your machine. 
3. Run the following commands to run the files:

- docker compose up -d
- python3 -m venv .venv
source .venv/bin/activate

- pip install -r requirements.txt

- pytest (optional)

- python main.py

## 🏗️ Project Architecture & Structure

```text
data-engineering-etl/
├── .vscode/
│   └── settings.json           # VS Code Python environment & formatting settings
├── config/
│   └── settings.py             # Database connection parameters & SQLAlchemy engine
├── src/
│   ├── extract/
│   │   └── generator.py        # Generates fake user data with Faker
│   ├── transform/
│   │   └── clean_data.py       # Data cleaning, formatting & feature engineering
│   └── load/
│       └── postgres_loader.py  # Loads transformed DataFrames to PostgreSQL
├── sql/
│   ├── create_tables.sql       # DDL schema definitions
│   └── analytical_queries.sql  # Sample analytical SQL queries
├── tests/
│   ├── test_extract.py         # Unit tests for extract generator
│   └── test_transform.py       # Unit tests for transform logic
├── .env.example                # Template environment variables file
├── .gitignore                  # Keeps secrets, cache, and virtual environment out of Git
├── docker-compose.yml          # PostgreSQL database container configuration
├── main.py                     # Pipeline orchestrator / entry point
└── requirements.txt            # Project dependencies