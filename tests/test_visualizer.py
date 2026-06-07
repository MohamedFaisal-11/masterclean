import pandas as pd

from masterclean.dashboard.visualizer import generate_charts


def test_chart_generation():

    df = pd.DataFrame({

        "age": [20, 25, 30],
        "salary": [1000, 2000, 3000]

    })

    charts = generate_charts(df)

    assert len(charts) > 0
