import plotly.express as px


def generate_charts(df):

    chart_html = ""

    # -----------------------------------
    # Numeric Charts
    # -----------------------------------

    numeric_columns = df.select_dtypes(
        include=["int64", "float64", "Int64"]
    ).columns

    for col in numeric_columns:

        try:

            # Histogram
            fig = px.histogram(
                df,
                x=col,
                title=f"{col} Distribution",
                template="plotly_dark"
            )

            chart_html += fig.to_html(
                full_html=False,
                include_plotlyjs="cdn"
            )

            # Boxplot
            fig = px.box(
                df,
                y=col,
                title=f"{col} Boxplot",
                template="plotly_dark"
            )

            chart_html += fig.to_html(
                full_html=False,
                include_plotlyjs=False
            )

        except:
            pass

    # -----------------------------------
    # Categorical Charts
    # -----------------------------------

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns

    for col in categorical_columns:

        try:

            value_counts = (
                df[col]
                .value_counts()
                .head(10)
            )

            # Bar Chart
            fig = px.bar(
                x=value_counts.index,
                y=value_counts.values,
                title=f"{col} Top Categories",
                labels={
                    "x": col,
                    "y": "Count"
                },
                template="plotly_dark"
            )

            chart_html += fig.to_html(
                full_html=False,
                include_plotlyjs=False
            )

            # Pie Chart
            fig = px.pie(
                values=value_counts.values,
                names=value_counts.index,
                title=f"{col} Distribution",
                template="plotly_dark"
            )

            chart_html += fig.to_html(
                full_html=False,
                include_plotlyjs=False
            )

        except:
            pass

    print("✅ Unified interactive charts generated")

    return chart_html