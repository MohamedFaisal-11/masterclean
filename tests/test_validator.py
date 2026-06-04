import pandas as pd

from masterclean.validator import validate_data


def test_negative_value_detection():

    data = {
        "age": [25, -5]
    }

    df = pd.DataFrame(data)

    warnings = validate_data(df)

    assert len(warnings) > 0