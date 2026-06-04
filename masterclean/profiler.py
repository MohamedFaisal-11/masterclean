import pandas as pd


def generate_profile(df):

    profile = {}

    # -----------------------------------
    # Dataset Summary
    # -----------------------------------

    profile["rows"] = df.shape[0]
    profile["columns"] = df.shape[1]

    profile["duplicate_rows"] = df.duplicated().sum()

    profile["memory_usage_mb"] = round(
        df.memory_usage(deep=True).sum() / 1024 / 1024,
        2
    )

    # -----------------------------------
    # Column Profiles
    # -----------------------------------

    column_profiles = {}

    for col in df.columns:

        column_data = {}

        column_data["dtype"] = str(df[col].dtype)

        column_data["missing_values"] = int(
            df[col].isnull().sum()
        )

        column_data["unique_values"] = int(
            df[col].nunique()
        )

        # -----------------------------------
        # Numeric Statistics
        # -----------------------------------

        if pd.api.types.is_numeric_dtype(df[col]):

            column_data["mean"] = round(
                df[col].mean(),
                2
            )

            column_data["median"] = round(
                df[col].median(),
                2
            )

            column_data["min"] = round(
                df[col].min(),
                2
            )

            column_data["max"] = round(
                df[col].max(),
                2
            )

            column_data["std"] = round(
                df[col].std(),
                2
            )

        # -----------------------------------
        # Categorical Statistics
        # -----------------------------------

        else:

            try:

                mode_value = df[col].mode()[0]

                mode_frequency = int(
                    (df[col] == mode_value).sum()
                )

                column_data["top_value"] = str(mode_value)

                column_data["top_frequency"] = mode_frequency

            except:

                column_data["top_value"] = "N/A"

                column_data["top_frequency"] = 0

        column_profiles[col] = column_data

    profile["column_profiles"] = column_profiles

    print("✅ Data profile generated")

    return profile