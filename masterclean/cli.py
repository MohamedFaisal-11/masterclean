import typer

from masterclean import (
    read_file,
    clean_data,
    export_data,
    optimize_dtypes
)

app = typer.Typer()

@app.command()
def clean(file_path: str):

    df = read_file(file_path)

    df = clean_data(df)

    df = optimize_dtypes(df)

    export_data(df)

    print("🎉 Cleaning completed successfully")


def main():
    app()


if __name__ == "__main__":
    main()