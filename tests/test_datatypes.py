import pandas as pd

from masterclean.preprocessing.datatypes import optimize_dtypes


def test_boolean_conversion():

    df = pd.DataFrame({

        "active": ["yes", "no", "yes"]

    })

    optimized_df = optimize_dtypes(df)

    assert optimized_df["active"].dtype == bool


def test_datetime_conversion():

    df = pd.DataFrame({

        "join_date": [
            "2024-01-01",
            "2024-02-01"
        ]

    })

    optimized_df = optimize_dtypes(df)

    assert str(
        optimized_df["join_date"].dtype
    ).startswith("datetime")


def test_category_conversion():

    df = pd.DataFrame({

        "city": [
            "Chennai",
            "Mumbai",
            "Chennai",
            "Mumbai"
        ]

    })

    optimized_df = optimize_dtypes(df)

    assert str(
        optimized_df["city"].dtype
    ) == "category"
