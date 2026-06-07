import pandas as pd

import plotly.express as px


def generate_charts(df):

    charts = []

    # -----------------------------------
    # Numeric Columns
    # -----------------------------------

    numeric_cols = df.select_dtypes(

        include=["int64", "float64", "Int64"]

    ).columns

    # -----------------------------------
    # Categorical Columns
    # -----------------------------------

    categorical_cols = df.select_dtypes(

        include=["object", "category"]

    ).columns

    # -----------------------------------
    # Plotly JS Loader
    # -----------------------------------

    plotly_loaded = False

    # -----------------------------------
    # Export Helper
    # -----------------------------------

    def export_chart(fig):

        nonlocal plotly_loaded

        fig.update_layout(

            autosize=True,

            hovermode="closest",

            template="plotly_white"

        )

        # -----------------------------------
        # Detect Chart Type
        # -----------------------------------

        try:

            chart_type = fig.data[0].type

        except:

            chart_type = ""

        # -----------------------------------
        # Pie Chart Hover
        # -----------------------------------

        if chart_type == "pie":

            fig.update_traces(

                hovertemplate=
                "<b>%{label}</b><br>"
                "Value: %{value}<br>"
                "Percentage: %{percent}"
                "<extra></extra>"

            )

        # -----------------------------------
        # Other Charts Hover
        # -----------------------------------

        else:

            fig.update_traces(

                hovertemplate=
                "<b>%{x}</b><br>"
                "Value: %{y}"
                "<extra></extra>"

            )

        # -----------------------------------
        # Export HTML
        # -----------------------------------

        html = fig.to_html(

            full_html=False,

            include_plotlyjs=(
                "cdn"
                if not plotly_loaded
                else False
            ),

            config={

                "responsive": True,

                "displayModeBar": True,

                "scrollZoom": True,

                "displaylogo": False

            }

        )

        plotly_loaded = True

        return html

    # -----------------------------------
    # 1. Correlation Heatmap
    # -----------------------------------

    if len(numeric_cols) >= 2:

        try:

            correlation_matrix = df[
                numeric_cols
            ].corr()

            fig = px.imshow(

                correlation_matrix,

                text_auto=True,

                color_continuous_scale="Blues",

                aspect="auto",

                title="Correlation Heatmap"

            )

            fig.update_layout(

                height=500

            )

            charts.append(

                export_chart(fig)

            )

        except:
            pass

    # -----------------------------------
    # 2. Histograms
    # -----------------------------------

    for col in numeric_cols[:3]:

        try:

            fig = px.histogram(

                df,

                x=col,

                nbins=30,

                title=f"{col} Distribution",

                marginal="box"

            )

            fig.update_layout(

                height=500,

                xaxis_title=col,

                yaxis_title="Count"

            )

            charts.append(

                export_chart(fig)

            )

        except:
            pass

    # -----------------------------------
    # 3. Boxplots
    # -----------------------------------

    for col in numeric_cols[:3]:

        try:

            fig = px.box(

                df,

                y=col,

                title=f"{col} Boxplot"

            )

            fig.update_layout(

                height=500,

                yaxis_title=col

            )

            charts.append(

                export_chart(fig)

            )

        except:
            pass

    # -----------------------------------
    # 4. Missing Values Chart
    # -----------------------------------

    try:

        missing_data = (

            df.isnull()
            .sum()
            .sort_values(ascending=False)

        )

        missing_data = missing_data[
            missing_data > 0
        ]

        if len(missing_data) > 0:

            fig = px.bar(

                x=missing_data.index,

                y=missing_data.values,

                title="Missing Values by Column",

                labels={

                    "x": "Columns",

                    "y": "Missing Count"

                }

            )

            fig.update_layout(

                height=500

            )

            charts.append(

                export_chart(fig)

            )

    except:
        pass

    # -----------------------------------
    # 5. Pie Charts
    # -----------------------------------

    for col in categorical_cols[:2]:

        try:

            value_counts = (

                df[col]
                .value_counts()
                .head(10)

            )

            fig = px.pie(

                names=value_counts.index,

                values=value_counts.values,

                title=f"{col} Distribution"

            )

            fig.update_layout(

                height=500

            )

            charts.append(

                export_chart(fig)

            )

        except:
            pass

    # -----------------------------------
    # 6. Bar Charts
    # -----------------------------------

    for col in categorical_cols[:2]:

        try:

            value_counts = (

                df[col]
                .value_counts()
                .head(10)

            )

            fig = px.bar(

                x=value_counts.index,

                y=value_counts.values,

                title=f"Top Categories in {col}",

                labels={

                    "x": col,

                    "y": "Count"

                }

            )

            fig.update_layout(

                height=500,

                xaxis_title=col,

                yaxis_title="Count"

            )

            charts.append(

                export_chart(fig)

            )

        except:
            pass

    # -----------------------------------
    # 7. Scatter Plot
    # -----------------------------------

    if len(numeric_cols) >= 2:

        try:

            scatter_df = df.dropna(

                subset=[

                    numeric_cols[0],

                    numeric_cols[1]

                ]

            )

            fig = px.scatter(

                scatter_df,

                x=numeric_cols[0],

                y=numeric_cols[1],

                title=f"{numeric_cols[0]} vs {numeric_cols[1]}",

                trendline="ols"

            )

            fig.update_layout(

                height=500,

                xaxis_title=numeric_cols[0],

                yaxis_title=numeric_cols[1]

            )

            charts.append(

                export_chart(fig)

            )

        except:
            pass

    # -----------------------------------
    # 8. Line Chart
    # -----------------------------------

    if len(numeric_cols) >= 1:

        try:

            line_df = df.copy()

            line_df = line_df.reset_index()

            line_df = line_df.dropna(

                subset=[numeric_cols[0]]

            )

            fig = px.line(

                line_df,

                x="index",

                y=numeric_cols[0],

                title=f"{numeric_cols[0]} Trend Analysis",

                markers=True

            )

            fig.update_traces(

                mode="lines+markers"

            )

            fig.update_layout(

                height=500,

                xaxis_title="Row Index",

                yaxis_title=numeric_cols[0]

            )

            charts.append(

                export_chart(fig)

            )

        except:
            pass

    print("✅ Advanced interactive charts generated")

    return charts
