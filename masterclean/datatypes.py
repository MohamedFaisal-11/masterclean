import pandas as pd


def optimize_dtypes(df):

    df = df.copy()

    for col in df.columns:

        # Skip already numeric columns
        if pd.api.types.is_numeric_dtype(df[col]):
            continue

        # Process only object columns
        if df[col].dtype == "object":

            # -----------------------------------
            # Intelligent Date Detection
            # -----------------------------------

            date_keywords = ["date", "time", "year"]

            is_date_column = any(
                keyword in col.lower()
                for keyword in date_keywords
            )

            if is_date_column:

                try:

                    converted = pd.to_datetime(
                        df[col],
                        errors="coerce"
                    )

                    if converted.notna().sum() > len(df) * 0.5:

                        df[col] = converted

                        continue

                except:
                    pass

            # -----------------------------------
            # Numeric Conversion
            # -----------------------------------

            try:

                converted = pd.to_numeric(
                    df[col],
                    errors="coerce"
                )

                if converted.notna().sum() > len(df) * 0.7:

                    df[col] = converted

            except:
                pass

    # Convert float columns into Int64 if possible
    for col in df.select_dtypes(include=['float']):

        try:

            if (df[col].dropna() % 1 == 0).all():

                df[col] = df[col].astype("Int64")

        except:
            pass

    print("✅ Datatypes optimized")

    return df