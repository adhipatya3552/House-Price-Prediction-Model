def feature_engineering(df):

    # Create useful features
    if 'RM' in df.columns and 'AGE' in df.columns:
        df['Rooms_per_Age'] = df['RM'] / (df['AGE'] + 1)
    if 'TAX' in df.columns and 'RM' in df.columns:
        df['Tax_per_Room'] = df['TAX'] / (df['RM'] + 1)

    return df