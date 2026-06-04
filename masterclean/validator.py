import pandas as pd


def validate_data(df):

    warnings = []

    # -----------------------------------
    # Negative Value Detection
    # -----------------------------------

    for col in df.select_dtypes(include=["int64", "float64", "Int64"]):

        try:

            negative_count = (df[col] < 0).sum()

            if negative_count > 0:

                warnings.append(
                    f"⚠ Negative values found in '{col}' ({negative_count} rows)"
                )

        except:
            pass

    # -----------------------------------
    # Outlier Detection (IQR Method)
    # -----------------------------------

    for col in df.select_dtypes(include=["int64", "float64", "Int64"]):

        try:

            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)

            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = df[
                (df[col] < lower_bound) |
                (df[col] > upper_bound)
            ]

            if len(outliers) > 0:

                warnings.append(
                    f"⚠ Possible outliers detected in '{col}' ({len(outliers)} rows)"
                )

        except:
            pass

    # -----------------------------------
    # Boolean Category Validation
    # -----------------------------------

    valid_boolean_values = {
        "true",
        "false",
        "yes",
        "no"
    }

    for col in df.select_dtypes(include="object"):

        unique_values = set(
            df[col]
            .dropna()
            .astype(str)
            .str.lower()
            .unique()
        )

        if (
            unique_values.intersection(valid_boolean_values)
            and not unique_values.issubset(valid_boolean_values)
        ):

            invalid_values = unique_values - valid_boolean_values

            warnings.append(
                f"⚠ Invalid boolean-like values found in '{col}': {invalid_values}"
            )

    # -----------------------------------
    # Print Validation Results
    # -----------------------------------

    if warnings:

        print("\nVALIDATION WARNINGS")
        print("=" * 40)

        for warning in warnings:
            print(warning)

    else:

        print("✅ No major validation issues found")

    return warnings