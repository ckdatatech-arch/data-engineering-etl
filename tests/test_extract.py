import pandas as pd
from src.extract.generator import generate_fake_users

def test_generate_fake_users_schema():
    """Verify generated dataset contains correct columns and row count."""
    df = generate_fake_users(num_records=10)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10

    expected_columns = {"user_id", "full_name", "email", "signup_date", "raw_country"}
    assert set(df.columns) == expected_columns