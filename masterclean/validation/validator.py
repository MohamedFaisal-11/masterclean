import re


def validate_data(df):

    warnings = []

    # -----------------------------------
    # Negative Values
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
    # Outlier Detection
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
    # Boolean Validation
    # -----------------------------------

    valid_boolean_values = {
        "true",
        "false",
        "yes",
        "no",
        "y",
        "n"
    }

    for col in df.select_dtypes(include="object"):

        try:

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

        except:
            pass

    # -----------------------------------
    # Null Percentage Validation
    # -----------------------------------

    for col in df.columns:

        try:

            null_percentage = (
                df[col].isnull().sum() / len(df)
            ) * 100

            if null_percentage > 30:

                warnings.append(
                    f"⚠ High missing values in '{col}' ({null_percentage:.1f}%)"
                )

        except:
            pass

    # -----------------------------------
    # Duplicate Row Validation
    # -----------------------------------

    try:

        duplicate_percentage = (
            df.duplicated().sum() / len(df)
        ) * 100

        if duplicate_percentage > 10:

            warnings.append(
                f"⚠ High duplicate rows detected ({duplicate_percentage:.1f}%)"
            )

    except:
        pass

    # -----------------------------------
    # Email Validation
    # -----------------------------------

    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    for col in df.select_dtypes(include="object"):

        try:

            if "email" in col.lower():

                invalid_emails = df[
                    ~df[col]
                    .fillna("")
                    .astype(str)
                    .str.match(email_pattern)
                ]

                if len(invalid_emails) > 0:

                    warnings.append(
                        f"⚠ Invalid email values found in '{col}' ({len(invalid_emails)} rows)"
                    )

        except:
            pass

    # -----------------------------------
    # Phone Number Validation
    # -----------------------------------

    phone_pattern = r"^\+?[0-9]{10,15}$"

    for col in df.select_dtypes(include="object"):

        try:

            if "phone" in col.lower():

                invalid_phones = df[
                    ~df[col]
                    .fillna("")
                    .astype(str)
                    .str.match(phone_pattern)
                ]

                if len(invalid_phones) > 0:

                    warnings.append(
                        f"⚠ Invalid phone numbers found in '{col}' ({len(invalid_phones)} rows)"
                    )

        except:
            pass

    # -----------------------------------
    # Mixed Datatype Detection
    # -----------------------------------

    for col in df.columns:

        try:

            types_found = df[col].dropna().map(type).nunique()

            if types_found > 1:

                warnings.append(
                    f"⚠ Mixed datatypes detected in '{col}'"
                )

        except:
            pass

    # -----------------------------------
    # Display Warnings
    # -----------------------------------

    if warnings:

        print("\nVALIDATION WARNINGS")
        print("=" * 40)

        for warning in warnings:

            print(warning)

    else:

        print("✅ No major validation issues found")

    return warnings
