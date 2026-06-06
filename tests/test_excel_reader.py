from masterclean.reader import read_file


def test_excel_reader():

    df = read_file("sample.xlsx")

    assert df is not None
