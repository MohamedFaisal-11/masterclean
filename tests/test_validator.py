import pandas as pd

from masterclean.validator import validate_data


def test_negative_values():

    df = pd.DataFrame({

        "age": [-5, 10]

    })

    warnings = validate_data(df)

    assert len(warnings) > 0