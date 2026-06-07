import pandas as pd


def clean_data(df):

    df = df.copy()

    # -----------------------------------
    # Standardize Column Names
    # -----------------------------------

    df.columns = [

        col.strip()
        .lower()
        .replace(" ", "_")

        for col in df.columns
    ]

    # -----------------------------------
    # Remove Duplicate Rows
    # -----------------------------------

    df = df.drop_duplicates()

    # -----------------------------------
    # Replace Empty Strings with NA
    # -----------------------------------

    df = df.replace(
        r'^\s*$',
        pd.NA,
        regex=True
    )

    # -----------------------------------
    # Clean Object Columns
    # -----------------------------------

    object_cols = df.select_dtypes(
        include="object"
    ).columns

    for col in object_cols:

        try:

            df[col] = (

                df[col]
                .astype(str)
                .str.strip()

            )

            # Restore missing values
            df[col] = df[col].replace(
                ["nan", "None", ""],
                pd.NA
            )

        except:
            pass

    # -----------------------------------
    # Datetime Conversion
    # -----------------------------------

    for col in df.columns:

        try:

            if (
                "date" in col.lower()
                or "time" in col.lower()
            ):

                df[col] = pd.to_datetime(

                    df[col],

                    errors="coerce",

                    dayfirst=True

                )

        except:
            pass

    # -----------------------------------
    # Fill Missing Numeric Values
    # -----------------------------------

    numeric_cols = df.select_dtypes(
        include=["int64", "float64", "Int64"]
    ).columns

    for col in numeric_cols:

        try:

            median_value = df[col].median()

            df[col] = df[col].fillna(
                median_value
            )

        except:
            pass

    # -----------------------------------
    # Fill Missing Categorical Values
    # -----------------------------------

    categorical_cols = df.select_dtypes(
        include="object"
    ).columns

    for col in categorical_cols:

        try:

            mode_value = df[col].mode()[0]

            df[col] = df[col].fillna(
                mode_value
            )

        except:
            pass

    # -----------------------------------
    # Remove Fully Empty Rows
    # -----------------------------------

    df = df.dropna(how="all")

    # -----------------------------------
    # Reset Index
    # -----------------------------------

    df = df.reset_index(drop=True)

    print("✅ Advanced data cleaning completed")

    return df
