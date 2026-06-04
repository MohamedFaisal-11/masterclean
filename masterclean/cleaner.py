def clean_data(df):

    df = df.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    for col in df.columns:

        # Object columns
        if df[col].dtype == "object":

            try:

                mode_value = df[col].mode()[0]

                df[col] = df[col].fillna(mode_value)

            except:
                pass

        # Numeric columns
        else:

            try:

                median_value = df[col].median()

                df[col] = df[col].fillna(median_value)

            except:
                pass

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Clean string columns
    for col in df.select_dtypes(include="object"):

        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
        )

    print("✅ Data cleaned successfully")

    return df