import pandas as pd

from masterclean.preprocessing.cleaner import clean_data


def test_missing_values():

    data = {
        "name": ["Ali", None],
        "age": [25, None]
    }

    df = pd.DataFrame(data)

    cleaned_df = clean_data(df)

    assert cleaned_df.isnull().sum().sum() == 0