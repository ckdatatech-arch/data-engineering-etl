import pandas as pd
from src.transform.clean_data import transform_user_data

def test_transform_user_data_cleaning():
    """Test string standardization and calculated fields."""
    raw_data = pd.DataFrame([{
        "user_id": "1234",
        "full_name": "john doe",
        "email": "JOHN.DOE@EXAMPLE.COM",
        "signup_date": "2024-01-01",
        "raw_country": "united states"
    }])

    transformed_df = transform_user_data(raw_data)

    # Assert string cleaning
    assert transformed_df.iloc[0]["full_name"] == "John Doe"
    assert transformed_df.iloc[0]["email"] == "john.doe@example.com"
    assert transformed_df.iloc[0]["country"] == "UNITED STATES"

    # Assert dropped columns and derived features
    assert "raw_country" not in transformed_df.columns
    assert "is_recent_signup" in transformed_df.columns