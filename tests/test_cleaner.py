import pandas as pd

from masterclean.cleaner import clean_data


def test_duplicate_removal():

    df = pd.DataFrame({

        "name": ["Ali", "Ali"],

        "age": [25, 25]

    })

    cleaned = clean_data(df)

    assert len(cleaned) == 1