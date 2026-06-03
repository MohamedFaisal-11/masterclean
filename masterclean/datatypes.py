import pandas as pd

def optimize_dtypes(df):

    df = df.copy()

    for col in df.columns:

        # Skip numeric columns
        if pd.api.types.is_numeric_dtype(df[col]):
            continue

        # Try converting only object/string columns
        if df[col].dtype == "object":

            # Try datetime conversion safely
            try:

                converted = pd.to_datetime(
                    df[col],
                    errors="raise"
                )

                # Accept conversion only if most values parsed
                if converted.notna().sum() > len(df) * 0.7:
                    df[col] = converted
                    continue

            except:
                pass

        # Try numeric conversion
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

    # Convert float columns with whole numbers into int
    for col in df.select_dtypes(include=['float']):

        if (df[col] % 1 == 0).all():
            df[col] = df[col].astype(int)

    print("✅ Datatypes optimized")

    return df