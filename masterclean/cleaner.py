def clean_data(df):

    # Create proper dataframe copy
    df = df.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    for col in df.columns:

        if df[col].dtype == "object":

            df.loc[:, col] = df[col].fillna(df[col].mode()[0])

        else:

            df.loc[:, col] = df[col].fillna(df[col].median())

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("✅ Data cleaned successfully")

    return df