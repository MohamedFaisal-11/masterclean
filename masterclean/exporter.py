def export_data(df, output_file="cleaned_data.csv"):

    df.to_csv(output_file, index=False)

    print(f"✅ Cleaned CSV exported as {output_file}")