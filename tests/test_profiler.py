import pandas as pd

from masterclean.validation.profiler import generate_profile


def test_profile_generation():

    df = pd.DataFrame({

        "name": ["John", "Alice"],
        "age": [25, 30]

    })

    profile = generate_profile(df)

    assert profile["rows"] == 2

    assert profile["columns"] == 2


def test_health_score():

    df = pd.DataFrame({

        "name": ["John", None],
        "age": [25, 25]

    })

    profile = generate_profile(df)

    assert "health_score" in profile