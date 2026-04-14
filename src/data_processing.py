import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df


def check_missing(df):
    print("Missing values:\n", df.isnull().sum())
    return df


def preprocess_data(path):
    df = load_data(path)

    # Fix column names (VERY IMPORTANT)
    df.columns = df.columns.str.strip().str.upper()

    df = check_missing(df)

    return df