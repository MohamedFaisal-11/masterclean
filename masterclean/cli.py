import typer

from masterclean import (
    read_file,
    clean_data,
    export_data,
    optimize_dtypes,
    generate_report,
    validate_data,
    generate_profile,
    generate_charts
)

app = typer.Typer()


def process_file(

    file_path: str,

    output: str = "cleaned_data.csv",

    report: bool = True,

    skip_validation: bool = False

):

    # -----------------------------------
    # Read File
    # -----------------------------------

    df = read_file(file_path)

    # -----------------------------------
    # Clean Data
    # -----------------------------------

    df = clean_data(df)

    # -----------------------------------
    # Optimize Datatypes
    # -----------------------------------

    df = optimize_dtypes(df)

    # -----------------------------------
    # Generate Profile
    # -----------------------------------

    profile = generate_profile(df)

    # -----------------------------------
    # Generate Interactive Charts
    # -----------------------------------

    charts = generate_charts(df)

    # -----------------------------------
    # Validation
    # -----------------------------------

    warnings = []

    if not skip_validation:

        warnings = validate_data(df)

    # -----------------------------------
    # Generate HTML Report
    # -----------------------------------

    if report:

        generate_report(
            df=df,
            warnings=warnings,
            profile=profile,
            charts=charts
        )

    # -----------------------------------
    # Export Cleaned Data
    # -----------------------------------

    export_data(df, output)

    print("🎉 Cleaning completed successfully")


@app.command()
def clean(

    file_path: str,

    output: str = "cleaned_data.csv",

    report: bool = True,

    skip_validation: bool = False

):

    """
    Clean and analyze CSV or Excel datasets.
    """

    process_file(
        file_path,
        output,
        report,
        skip_validation
    )


@app.command()
def version():

    """
    Show current MasterClean version.
    """

    print("MasterClean v0.9-beta")


def main():

    app()


if __name__ == "__main__":

    main()