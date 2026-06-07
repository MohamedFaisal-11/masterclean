import pandas as pd


def generate_profile(df):

    profile = {}

    # -----------------------------------
    # Basic Information
    # -----------------------------------

    profile["rows"] = len(df)

    profile["columns"] = len(df.columns)

    profile["missing_values"] = int(
        df.isnull().sum().sum()
    )

    profile["duplicate_rows"] = int(
        df.duplicated().sum()
    )

    profile["memory_usage_mb"] = round(
        df.memory_usage(deep=True).sum() / 1024 / 1024,
        2
    )

    # -----------------------------------
    # Datatype Summary
    # -----------------------------------

    profile["datatypes"] = (
        df.dtypes
        .astype(str)
        .value_counts()
        .to_dict()
    )

    # -----------------------------------
    # Missing Values by Column
    # -----------------------------------

    missing_summary = {}

    for col in df.columns:

        missing_count = int(
            df[col].isnull().sum()
        )

        if missing_count > 0:

            missing_summary[col] = missing_count

    profile["missing_summary"] = missing_summary

    # -----------------------------------
    # Numeric Statistics
    # -----------------------------------

    numeric_profile = {}

    numeric_cols = df.select_dtypes(
        include=["int64", "float64", "Int64"]
    )

    for col in numeric_cols.columns:

        try:

            numeric_profile[col] = {

                "mean": round(
                    float(
                        numeric_cols[col].mean()
                    ),
                    2
                ),

                "median": round(
                    float(
                        numeric_cols[col].median()
                    ),
                    2
                ),

                "min": round(
                    float(
                        numeric_cols[col].min()
                    ),
                    2
                ),

                "max": round(
                    float(
                        numeric_cols[col].max()
                    ),
                    2
                )

            }

        except:
            pass

    profile["numeric_summary"] = numeric_profile

    # -----------------------------------
    # Categorical Summary
    # -----------------------------------

    categorical_profile = {}

    categorical_cols = df.select_dtypes(
        include="object"
    )

    for col in categorical_cols.columns:

        try:

            categorical_profile[col] = {

                "unique_values": int(
                    df[col].nunique()
                ),

                "top_value": str(
                    df[col].mode()[0]
                )

            }

        except:
            pass

    profile["categorical_summary"] = categorical_profile

    # -----------------------------------
    # Dataset Health Score
    # -----------------------------------

    health_score = 100

    try:

        null_percentage = (

            df.isnull().sum().sum()

            /

            (df.shape[0] * df.shape[1])

        ) * 100

        duplicate_percentage = (

            df.duplicated().sum()

            / len(df)

        ) * 100

        health_score -= int(
            null_percentage
        )

        health_score -= int(
            duplicate_percentage
        )

        health_score = max(
            0,
            health_score
        )

    except:
        pass

    profile["health_score"] = health_score

    print("✅ Advanced data profile generated")

    return profile
