import pandas as pd

from masterclean.validation.validator import validate_data


def test_negative_values():

    df = pd.DataFrame({

        "salary": [1000, -500, 2000]

    })

    warnings = validate_data(df)

    assert any(
        "Negative values" in warning
        for warning in warnings
    )


def test_duplicate_detection():

    df = pd.DataFrame({

        "name": ["A", "A", "A"],
        "age": [25, 25, 25]

    })

    warnings = validate_data(df)

    assert any(
        "duplicate rows" in warning.lower()
        for warning in warnings
    )


def test_invalid_email_detection():

    df = pd.DataFrame({

        "email": [
            "test@gmail.com",
            "wrong_email",
            "abc@"
        ]

    })

    warnings = validate_data(df)

    assert any(
        "Invalid email" in warning
        for warning in warnings
    )


def test_invalid_phone_detection():

    df = pd.DataFrame({

        "phone": [
            "9876543210",
            "123",
            "abcdef"
        ]

    })

    warnings = validate_data(df)

    assert any(
        "Invalid phone" in warning
        for warning in warnings
    )


def test_mixed_datatype_detection():

    df = pd.DataFrame({

        "age": [25, "Thirty", 40]

    })

    warnings = validate_data(df)

    assert any(
        "Mixed datatypes" in warning
        for warning in warnings
    )
