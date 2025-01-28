import pandas as pd
import os

def load_raw_data(filepath):
    """Load raw dataset from CSV file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"❌ ERROR: File not found at {os.path.abspath(filepath)}")
    return pd.read_csv(filepath, sep=";")

def clean_data(df):
    """Clean dataset (handle missing values, map categories)."""
    category_mapping = {1: 'Product', 2: 'Deal/Promotion', 3: 'Information'}
    df['Category_Name'] = df['Category'].map(category_mapping)
    
    # Fill missing values (optional)
    df.fillna(0, inplace=True)
    
    return df

def save_cleaned_data(df, filepath):
    """Save cleaned dataset to processed folder."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"✅ Cleaned dataset saved at: {filepath}")
