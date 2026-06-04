import pandas as pd

from masterclean.datatypes import optimize_dtypes


def test_numeric_conversion():

    data = {
        "salary": ["1000", "2000", "3000"]
    }

    df = pd.DataFrame(data)

    optimized_df = optimize_dtypes(df)

    assert str(optimized_df["salary"].dtype) in ["int64", "Int64"]