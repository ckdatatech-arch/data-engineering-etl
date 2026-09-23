# Data cleaning, formatting, filtering logic
import pandas as pd

def transform_user_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans, formats, and enriches raw user data."""
    df = df.copy()

    # Standardize string formatting
    df["full_name"] = df["full_name"].str.title()
    df["email"] = df["email"].str.lower()
    df["country"] = df["raw_country"].str.upper()

    # Derive new features
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    df["is_recent_signup"] = df["signup_date"] >= (pd.Timestamp.now() - pd.Timedelta(days=180))

    # Drop raw unneeded columns
    df.drop(columns=["raw_country"], inplace=True)

    return df