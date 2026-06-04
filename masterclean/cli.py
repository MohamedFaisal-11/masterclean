import typer

from masterclean import (
    read_file,
    clean_data,
    export_data,
    optimize_dtypes,
    generate_report,
    validate_data
)

app = typer.Typer()

@app.command()
def clean(file_path: str):

    df = read_file(file_path)

    df = clean_data(df)

    df = optimize_dtypes(df)

    validate_data(df)

    generate_report(df)

    export_data(df)

    print("🎉 Cleaning completed successfully")


def main():
    app()


if __name__ == "__main__":
    main()