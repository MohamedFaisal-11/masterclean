from masterclean import (
    read_file,
    clean_data,
    optimize_dtypes,
    validate_data,
    generate_profile,
    generate_charts,
    generate_report,
    export_data
)

# Read dataset
df = read_file("examples/sample.csv")

# Clean dataset
df = clean_data(df)

# Optimize datatypes
df = optimize_dtypes(df)

# Validate dataset
warnings = validate_data(df)

# Generate profile
profile = generate_profile(df)

# Generate charts
charts = generate_charts(df)

# Generate report
generate_report(
    df=df,
    warnings=warnings,
    profile=profile,
    charts=charts
)

# Export cleaned dataset
export_data(df)

print("MasterClean pipeline completed successfully")