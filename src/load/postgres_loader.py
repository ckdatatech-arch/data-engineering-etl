# Connects and inserts transformed data into PostgreSQL
import pandas as pd
from config.settings import get_db_engine

def load_to_postgres(df: pd.DataFrame, table_name: str = "dim_users") -> None:
    """Loads transformed Pandas DataFrame into PostgreSQL database."""
    engine = get_db_engine()
    
    with engine.begin() as connection:
        df.to_sql(
            name=table_name,
            con=connection,
            if_exists="replace",  # Use 'append' in production
            index=False
        )
    print(f"Successfully loaded {len(df)} rows into table '{table_name}'.")