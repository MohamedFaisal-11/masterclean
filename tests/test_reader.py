import pandas as pd

from masterclean.utils.reader import read_file


def test_csv_reading():

    df = pd.DataFrame({

        "name": ["John", "Alice"],
        "age": [25, 30]

    })

    df.to_csv(
        "test_sample.csv",
        index=False
    )

    loaded_df, extension = read_file(
        "test_sample.csv"
    )

    assert loaded_df is not None

    assert extension == ".csv"


def test_excel_reading():

    df = pd.DataFrame({

        "name": ["John", "Alice"],
        "age": [25, 30]

    })

    df.to_excel(
        "test_sample.xlsx",
        index=False
    )

    loaded_df, extension = read_file(
        "test_sample.xlsx"
    )

    assert loaded_df is not None

    assert extension == ".xlsx"


def test_invalid_file_format():

    result = read_file(
        "invalid_file.txt"
    )

    assert result is None
