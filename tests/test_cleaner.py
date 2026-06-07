import pandas as pd

from masterclean.preprocessing.cleaner import clean_data


def test_duplicate_removal():

    df = pd.DataFrame({

        "name": ["A", "A", "B"],
        "age": [25, 25, 30]

    })

    cleaned_df = clean_data(df)

    assert len(cleaned_df) == 2


def test_column_standardization():

    df = pd.DataFrame({

        "First Name": ["John"],
        "Last Name": ["Doe"]

    })

    cleaned_df = clean_data(df)

    assert "first_name" in cleaned_df.columns
    assert "last_name" in cleaned_df.columns


def test_empty_string_cleanup():

    df = pd.DataFrame({

        "name": ["John", "", "Alice"]

    })

    cleaned_df = clean_data(df)

    assert (
        cleaned_df["name"]
        .astype(str)
        .str.contains("<NA>")
        .sum()
    ) >= 1



def test_numeric_missing_fill():

    df = pd.DataFrame({

        "salary": [1000, None, 3000]

    })

    cleaned_df = clean_data(df)

    assert cleaned_df["salary"].isnull().sum() == 0


def test_categorical_missing_fill():

    df = pd.DataFrame({

        "city": ["Chennai", None, "Mumbai"]

    })

    cleaned_df = clean_data(df)

    assert cleaned_df["city"].isnull().sum() == 0


def test_datetime_conversion():

    df = pd.DataFrame({

        "join_date": [
            "2024-01-01",
            "2024-02-01"
        ]

    })

    cleaned_df = clean_data(df)

    assert str(
        cleaned_df["join_date"].dtype
    ).startswith("datetime")
