import pandas as pd

from masterclean.cleaner import clean_data


def test_duplicate_removal():

    data = {
        "name": ["Ali", "Ali"],
        "age": [25, 25]
    }

    df = pd.DataFrame(data)

    cleaned_df = clean_data(df)

    assert len(cleaned_df) == 1