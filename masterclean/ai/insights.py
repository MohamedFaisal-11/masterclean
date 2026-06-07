import pandas as pd
import pandas as pd


def generate_ai_insights(df):

    insights = []

    summary_points = []

    # -----------------------------------
    # Missing Value Insights
    # -----------------------------------

    total_missing = df.isnull().sum().sum()

    for col in df.columns:

        missing_percentage = (

            df[col].isnull().sum()

            / len(df)

        ) * 100

        if missing_percentage > 20:

            insights.append(

                f"⚠ Column '{col}' contains "
                f"{missing_percentage:.1f}% missing values."

            )

            insights.append(

                "💡 Recommendation: "
                "Consider median/mode imputation."

            )

            summary_points.append(

                f"high missing values detected in '{col}'"

            )

    # -----------------------------------
    # Numeric Insights
    # -----------------------------------

    numeric_cols = df.select_dtypes(

        include=["int64", "float64", "Int64"]

    ).columns

    for col in numeric_cols:

        try:

            skewness = df[col].skew()

            if skewness > 1:

                insights.append(

                    f"📈 '{col}' is highly right-skewed."

                )

                insights.append(

                    "💡 Recommendation: "
                    "Consider log transformation."

                )

                summary_points.append(

                    f"'{col}' distribution is heavily right-skewed"

                )

            elif skewness < -1:

                insights.append(

                    f"📉 '{col}' is highly left-skewed."

                )

                summary_points.append(

                    f"'{col}' distribution is heavily left-skewed"

                )

        except:
            pass

    # -----------------------------------
    # Outlier Insights
    # -----------------------------------

    for col in numeric_cols:

        try:

            Q1 = df[col].quantile(0.25)

            Q3 = df[col].quantile(0.75)

            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR

            upper = Q3 + 1.5 * IQR

            outliers = df[
                (df[col] < lower)
                |
                (df[col] > upper)
            ]

            if len(outliers) > 0:

                insights.append(

                    f"🚨 Extreme outliers detected in '{col}'."

                )

                if "salary" in col.lower():

                    insights.append(

                        "💡 Possible cause: "
                        "Payroll entry issue or currency mismatch."

                    )

                elif "age" in col.lower():

                    insights.append(

                        "💡 Possible cause: "
                        "Invalid demographic values detected."

                    )

                elif "price" in col.lower():

                    insights.append(

                        "💡 Possible cause: "
                        "Incorrect pricing or unit mismatch."

                    )

                elif "sales" in col.lower():

                    insights.append(

                        "💡 Possible cause: "
                        "Abnormal sales spikes detected."

                    )

                else:

                    insights.append(

                        "💡 Recommendation: "
                        "Review abnormal values carefully."

                    )

                summary_points.append(

                    f"extreme outliers found in '{col}'"

                )

        except:
            pass

    # -----------------------------------
    # Correlation Intelligence
    # -----------------------------------

    try:

        correlation_matrix = df[
            numeric_cols
        ].corr()

        for col in correlation_matrix.columns:

            for idx in correlation_matrix.index:

                if col != idx:

                    corr_value = correlation_matrix.loc[idx, col]

                    if abs(corr_value) > 0.8:

                        insights.append(

                            f"📊 Strong correlation detected "
                            f"between '{col}' and '{idx}'."

                        )

                        summary_points.append(

                            f"strong correlation between "
                            f"'{col}' and '{idx}'"

                        )

        insights = list(dict.fromkeys(insights))

    except:
        pass

    # -----------------------------------
    # Categorical Dominance
    # -----------------------------------

    categorical_cols = df.select_dtypes(

        include=["object", "category"]

    ).columns

    for col in categorical_cols:

        try:

            top_percentage = (

                df[col]
                .value_counts(normalize=True)
                .iloc[0]

            ) * 100

            top_value = (

                df[col]
                .mode()[0]

            )

            if top_percentage > 70:

                insights.append(

                    f"📊 '{col}' is dominated by "
                    f"'{top_value}' "
                    f"({top_percentage:.1f}%)."

                )

                summary_points.append(

                    f"'{col}' is heavily dominated "
                    f"by '{top_value}'"

                )

        except:
            pass

    # -----------------------------------
    # Zero Variance Detection
    # -----------------------------------

    for col in df.columns:

        try:

            unique_values = df[col].nunique()

            if unique_values <= 1:

                insights.append(

                    f"⚠ '{col}' contains only "
                    f"one unique value."

                )

                insights.append(

                    "💡 Recommendation: "
                    "Remove low-information columns."

                )

                summary_points.append(

                    f"low variance detected in '{col}'"

                )

        except:
            pass

    # -----------------------------------
    # High Cardinality Detection
    # -----------------------------------

    categorical_cols = df.select_dtypes(

        include=["object", "category"]

    ).columns

    for col in categorical_cols:

        try:

            unique_ratio = (

                df[col].nunique()

                / len(df)

            ) * 100

            if unique_ratio > 85:

                insights.append(

                    f"⚠ '{col}' has extremely "
                    f"high uniqueness."

                )

                insights.append(

                    "💡 Recommendation: "
                    "Consider encoding strategies."

                )

                summary_points.append(

                    f"high cardinality detected in '{col}'"

                )

        except:
            pass

    # -----------------------------------
    # Identifier Column Detection
    # -----------------------------------

    for col in df.columns:

        try:

            unique_ratio = (

                df[col].nunique()

                / len(df)

            ) * 100

            if (

                unique_ratio > 95

                and

                (
                    "id" in col.lower()
                    or
                    "code" in col.lower()
                    or
                    "number" in col.lower()
                )

            ):

                insights.append(

                    f"📌 '{col}' appears to be "
                    f"a unique identifier column."

                )

                insights.append(

                    "💡 Recommendation: "
                    "Exclude from ML training."

                )

                summary_points.append(

                    f"identifier column detected in '{col}'"

                )

        except:
            pass

    # -----------------------------------
    # ML Readiness Insight
    # -----------------------------------

    if len(numeric_cols) >= 2:

        insights.append(

            "🤖 Dataset appears suitable "
            "for machine learning workflows."

        )

    # -----------------------------------
    # Dataset Health Insight
    # -----------------------------------

    duplicate_rows = df.duplicated().sum()

    if total_missing == 0 and duplicate_rows == 0:

        insights.append(

            "✅ Dataset quality looks very good."

        )

    # -----------------------------------
    # AI Summary Generation
    # -----------------------------------

    if summary_points:

        ai_summary = (

            "🧠 AI Summary: "
            + ", ".join(summary_points[:5])
            + "."

        )

    else:

        ai_summary = (

            "🧠 AI Summary: "
            "Dataset appears relatively clean "
            "with minimal quality concerns."

        )

    insights.insert(0, ai_summary)

    # -----------------------------------
    # AI Risk Scoring
    # -----------------------------------

    risk_score = 0

    missing_percentage_total = (

        total_missing

        /

        (df.shape[0] * df.shape[1])

    ) * 100

    if missing_percentage_total > 30:

        risk_score += 40

    elif missing_percentage_total > 15:

        risk_score += 25

    elif missing_percentage_total > 5:

        risk_score += 10

    # Column-level missing severity

    for col in df.columns:

        col_missing_percentage = (

            df[col].isnull().sum()

            / len(df)

        ) * 100

        if col_missing_percentage > 50:

            risk_score += 25

        elif col_missing_percentage > 30:

            risk_score += 15

        elif col_missing_percentage > 15:

            risk_score += 8

    # Duplicate Risk

    duplicate_percentage = (

        duplicate_rows

        / len(df)

    ) * 100

    if duplicate_percentage > 20:

        risk_score += 25

    elif duplicate_percentage > 10:

        risk_score += 15

    elif duplicate_percentage > 0:

        risk_score += 5

    # Quality Complexity Risk

    if len(summary_points) > 10:

        risk_score += 25

    elif len(summary_points) > 5:

        risk_score += 15

    elif len(summary_points) > 2:

        risk_score += 8

    # Dataset Complexity

    if len(df.columns) > 20:

        risk_score += 10

    risk_score = min(
        risk_score,
        100
    )

    # -----------------------------------
    # Risk Level Classification
    # -----------------------------------

    if risk_score >= 70:

        risk_level = "HIGH"

    elif risk_score >= 40:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    insights.insert(

        1,

        f"🚨 DATA RISK SCORE: "
        f"{risk_score}/100 "
        f"({risk_level} RISK)"

    )

    # -----------------------------------
    # Data Quality Grade
    # -----------------------------------

    if risk_score <= 20:

        quality_grade = "A"

    elif risk_score <= 40:

        quality_grade = "B"

    elif risk_score <= 60:

        quality_grade = "C"

    elif risk_score <= 80:

        quality_grade = "D"

    else:

        quality_grade = "F"

    insights.insert(

        2,

        f"📊 DATA QUALITY GRADE: {quality_grade}"

    )

    # -----------------------------------
    # Final Output
    # -----------------------------------

    print("\nAI INSIGHTS")
    print("=" * 40)

    for insight in insights:

        print(insight)

    return insights
