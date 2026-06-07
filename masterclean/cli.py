
import typer

from masterclean import (
    read_file,
    clean_data,
    export_data,
    optimize_dtypes,
    generate_report,
    validate_data,
    generate_profile,
    generate_charts,
    generate_ai_insights,
    detect_anomalies,
    generate_anomaly_chart
)

app = typer.Typer(
    help="🚀 MasterClean Enterprise AI Data Cleaning Platform"
)


# =========================================================
# COMMON DATA LOADER
# =========================================================

def load_dataset(file_path: str):

    """
    Load dataset safely.
    """

    try:

        result = read_file(file_path)

        if result is None:

            print("❌ Failed to load dataset")

            return None, None

        df, extension = result

        return df, extension

    except Exception as error:

        print(f"❌ File loading failed: {error}")

        return None, None


# =========================================================
# MAIN PROCESSING PIPELINE
# =========================================================

def process_file(

    file_path: str,

    output: str = "cleaned_data",

    report: bool = True,

    skip_validation: bool = False

):

    try:

        # =====================================================
        # LOAD DATASET
        # =====================================================

        df, file_extension = load_dataset(file_path)

        if df is None:

            return

        # =====================================================
        # DATA CLEANING
        # =====================================================

        df = clean_data(df)

        # =====================================================
        # DATATYPE OPTIMIZATION
        # =====================================================

        df = optimize_dtypes(df)

        # =====================================================
        # DATA PROFILE
        # =====================================================

        profile = generate_profile(df)

        # =====================================================
        # VISUALIZATIONS
        # =====================================================

        charts = generate_charts(df)

        # =====================================================
        # ANOMALY DETECTION
        # =====================================================

        anomalies = detect_anomalies(df)

        # =====================================================
        # ANOMALY VISUALIZATION
        # =====================================================

        anomaly_chart = generate_anomaly_chart(df)

        if anomaly_chart:

            charts.append(anomaly_chart)

        # =====================================================
        # DATA VALIDATION
        # =====================================================

        warnings = []

        if not skip_validation:

            warnings = validate_data(df)

        # =====================================================
        # AI INSIGHTS
        # =====================================================

        ai_insights = generate_ai_insights(df)

        # =====================================================
        # REPORT GENERATION
        # =====================================================

        if report:

            generate_report(

                df=df,

                warnings=warnings,

                profile=profile,

                charts=charts,

                ai_insights=ai_insights,

                anomalies=anomalies

            )

        # =====================================================
        # EXPORT CLEANED DATA
        # =====================================================

        export_data(

            df,

            output,

            file_extension

        )

        print("\n🎉 Cleaning completed successfully")

    except Exception as error:

        print(f"\n❌ Processing failed: {error}")


# =========================================================
# CLEAN COMMAND
# =========================================================

@app.command()
def clean(

    file_path: str,

    output: str = "cleaned_data",

    report: bool = True,

    skip_validation: bool = False

):

    """
    Clean, validate, analyze, and export datasets.
    """

    process_file(

        file_path=file_path,

        output=output,

        report=report,

        skip_validation=skip_validation

    )


# =========================================================
# VALIDATE COMMAND
# =========================================================

@app.command()
def validate(file_path: str):

    """
    Validate dataset quality.
    """

    try:

        df, _ = load_dataset(file_path)

        if df is None:

            return

        validate_data(df)

    except Exception as error:

        print(f"❌ Validation failed: {error}")


# =========================================================
# PROFILE COMMAND
# =========================================================

@app.command()
def profile(file_path: str):

    """
    Generate detailed dataset profile.
    """

    try:

        df, _ = load_dataset(file_path)

        if df is None:

            return

        profile_data = generate_profile(df)

        print("\n📊 DATA PROFILE")
        print("=" * 50)

        for key, value in profile_data.items():

            print(f"{key}: {value}")

    except Exception as error:

        print(f"❌ Profile generation failed: {error}")


# =========================================================
# DASHBOARD COMMAND
# =========================================================

@app.command()
def dashboard(file_path: str):

    """
    Generate enterprise AI dashboard.
    """

    try:

        df, _ = load_dataset(file_path)

        if df is None:

            return

        # =====================================================
        # PROFILE
        # =====================================================

        profile = generate_profile(df)

        # =====================================================
        # CHARTS
        # =====================================================

        charts = generate_charts(df)

        # =====================================================
        # ANOMALIES
        # =====================================================

        anomalies = detect_anomalies(df)

        # =====================================================
        # ANOMALY CHART
        # =====================================================

        anomaly_chart = generate_anomaly_chart(df)

        if anomaly_chart:

            charts.append(anomaly_chart)

        # =====================================================
        # VALIDATION
        # =====================================================

        warnings = validate_data(df)

        # =====================================================
        # AI INSIGHTS
        # =====================================================

        ai_insights = generate_ai_insights(df)

        # =====================================================
        # REPORT
        # =====================================================

        generate_report(

            df=df,

            warnings=warnings,

            profile=profile,

            charts=charts,

            ai_insights=ai_insights,

            anomalies=anomalies

        )

        print("\n✅ Enterprise dashboard generated successfully")

    except Exception as error:

        print(f"\n❌ Dashboard generation failed: {error}")


# =========================================================
# ANOMALY COMMAND
# =========================================================

@app.command()
def anomaly(file_path: str):

    """
    Detect anomalies in datasets.
    """

    try:

        df, _ = load_dataset(file_path)

        if df is None:

            return

        detect_anomalies(df)

    except Exception as error:

        print(f"❌ Anomaly detection failed: {error}")


# =========================================================
# VERSION COMMAND
# =========================================================

@app.command()
def version():

    """
    Show MasterClean version.
    """

    print("🚀 MasterClean v2.0.0-dev")


# =========================================================
# MAIN ENTRY
# =========================================================

def main():

    app()


if __name__ == "__main__":

    main()
