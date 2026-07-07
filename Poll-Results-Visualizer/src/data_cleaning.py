def clean_data(df):
    df = df.copy()

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Standardize text
    df['age_group'] = df['age_group'].str.strip()
    df['region'] = df['region'].str.strip()
    df['response'] = df['response'].str.strip()

    return df