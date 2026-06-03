from masterclean import read_file, clean_data, export_data

df = read_file("sample.csv")

cleaned_df = clean_data(df)

export_data(cleaned_df)