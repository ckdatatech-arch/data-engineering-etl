# Generates fake data using Faker library
import pandas as pd
from faker import Faker

def generate_fake_users(num_records: int = 100) -> pd.DataFrame:
    """Generates synthetic user data using Faker."""
    fake = Faker()
    data = []

    for _ in range(num_records):
        data.append({
            "user_id": fake.uuid4(),
            "full_name": fake.name(),
            "email": fake.email(),
            "signup_date": fake.date_between(start_date="-2y", end_date="today"),
            "raw_country": fake.country()
        })

    return pd.DataFrame(data)