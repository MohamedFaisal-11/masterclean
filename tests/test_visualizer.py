import pandas as pd

from masterclean.visualizer import generate_charts


def test_chart_generation():

    df = pd.DataFrame({

        "salary": [100, 200, 300]

    })

    charts = generate_charts(df)

    assert charts is not None