import pandas as pd

from masterclean.profiler import generate_profile


def test_profile_generation():

    df = pd.DataFrame({

        "salary": [100, 200, 300]

    })

    profile = generate_profile(df)

    assert "rows" in profile

    assert "column_profiles" in profile