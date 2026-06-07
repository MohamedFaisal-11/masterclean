def export_data(df, output_file, file_extension):

    # -----------------------------------
    # CSV Export
    # -----------------------------------

    if file_extension == ".csv":

        export_path = f"{output_file}.csv"

        df.to_csv(
            export_path,
            index=False
        )

        print(f"✅ Cleaned CSV exported as {export_path}")

    # -----------------------------------
    # Excel Export
    # -----------------------------------

    elif file_extension in [".xlsx", ".xls"]:

        export_path = f"{output_file}.xlsx"

        df.to_excel(
            export_path,
            index=False
        )

        print(f"✅ Cleaned Excel exported as {export_path}")

    # -----------------------------------
    # Unsupported Export
    # -----------------------------------

    else:

        print("❌ Unsupported export format")
