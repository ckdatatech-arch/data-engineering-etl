
from src.extract.generator import generate_fake_users
from src.transform.clean_data import transform_user_data
from src.load.postgres_loader import load_to_postgres

def run_pipeline():
    print("Starting ETL Pipeline...")

    # Extract (Generate Faker Data)
    print(" Extracting raw fake data...")
    raw_df = generate_fake_users(num_records=500)

    # Transform
    print(" Transforming and cleaning data...")
    clean_df = transform_user_data(raw_df)

    # Load
    print("Loading clean data to PostgreSQL...")
    load_to_postgres(clean_df, table_name="dim_users")

    print("ETL Pipeline executed successfully!")

if __name__ == "__main__":
    run_pipeline()