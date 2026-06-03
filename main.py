from masterclean import (
    read_file,
    clean_data,
    export_data,
    optimize_dtypes
)

df = read_file("sample.csv")

df = clean_data(df)

df = optimize_dtypes(df)

export_data(df)