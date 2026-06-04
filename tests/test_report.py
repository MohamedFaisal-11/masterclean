import pandas as pd

from masterclean.report import generate_report


def test_report_generation():

    df = pd.DataFrame({

        "age": [20, 30]

    })

    generate_report(df)

    assert True