import os
import pandas as pd

from masterclean.utils.exporter import export_data


def test_csv_export():

    df = pd.DataFrame({

        "name": ["John", "Alice"],
        "age": [25, 30]

    })

    export_data(
        df,
        "test_cleaned",
        ".csv"
    )

    assert os.path.exists(
        "test_cleaned.csv"
    )


def test_excel_export():

    df = pd.DataFrame({

        "name": ["John", "Alice"],
        "age": [25, 30]

    })

    export_data(
        df,
        "test_cleaned",
        ".xlsx"
    )

    assert os.path.exists(
        "test_cleaned.xlsx"
    )
