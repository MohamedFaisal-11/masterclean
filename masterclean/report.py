def generate_report(df, output_file="report.txt"):

    report = []

    report.append("MASTERCLEAN REPORT")
    report.append("=" * 40)

    report.append(f"Rows: {df.shape[0]}")
    report.append(f"Columns: {df.shape[1]}")

    report.append("\nCOLUMN TYPES")
    report.append("-" * 40)

    for col in df.columns:
        report.append(f"{col}: {df[col].dtype}")

    report.append("\nMISSING VALUES")
    report.append("-" * 40)

    missing = df.isnull().sum()

    for col, value in missing.items():
        report.append(f"{col}: {value}")

    with open(output_file, "w") as file:
        file.write("\n".join(report))

    print(f"✅ Report generated as {output_file}")