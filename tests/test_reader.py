from masterclean.reader import read_file


def test_csv_loading():

    df = read_file("tests/sample.csv")

    assert df is not None

    assert len(df) > 0