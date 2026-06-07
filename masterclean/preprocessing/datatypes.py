import pandas as pd


def optimize_dtypes(df):

    df = df.copy()

    # -----------------------------------
    # Numeric Optimization
    # -----------------------------------

    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    for col in numeric_cols:

        try:

            df[col] = pd.to_numeric(
                df[col],
                downcast="integer"
            )

            df[col] = pd.to_numeric(
                df[col],
                downcast="float"
            )

        except:
            pass

    # -----------------------------------
    # Boolean Conversion
    # -----------------------------------

    boolean_map = {

        "true": True,
        "false": False,
        "yes": True,
        "no": False,
        "y": True,
        "n": False

    }

    object_cols = df.select_dtypes(
        include="object"
    ).columns

    for col in object_cols:

        try:

            unique_values = set(
                df[col]
                .dropna()
                .astype(str)
                .str.lower()
                .unique()
            )

            if unique_values.issubset(
                boolean_map.keys()
            ):

                df[col] = (
                    df[col]
                    .astype(str)
                    .str.lower()
                    .map(boolean_map)
                )

        except:
            pass

    # -----------------------------------
    # Datetime Detection
    # -----------------------------------

    for col in df.columns:

        try:

            if "date" in col.lower():

                df[col] = pd.to_datetime(
                    df[col],
                    errors="coerce"
                )

        except:
            pass

    # -----------------------------------
    # Category Optimization
    # -----------------------------------

    for col in object_cols:

        try:

            unique_ratio = (
                df[col].nunique()
                / len(df)
            )

            if unique_ratio <= 0.5:

                df[col] = df[col].astype(
                    "category"
                )

        except:
            pass

    print("✅ Datatypes optimized successfully")

    return df
