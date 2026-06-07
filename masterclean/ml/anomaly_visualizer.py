import plotly.express as px

from scipy.stats import zscore


def generate_anomaly_chart(df):

    # =====================================================
    # NUMERIC COLUMNS
    # =====================================================

    numeric_cols = df.select_dtypes(

        include="number"

    ).columns

    # Need minimum 2 numeric columns
    if len(numeric_cols) < 2:

        return None

    try:

        # =====================================================
        # SELECT COLUMNS
        # =====================================================

        x_col = numeric_cols[0]

        y_col = numeric_cols[1]

        # =====================================================
        # Z-SCORE ANOMALY DETECTION
        # =====================================================

        z_scores_x = zscore(df[x_col].fillna(0))

        z_scores_y = zscore(df[y_col].fillna(0))

        anomaly_mask = (

            (abs(z_scores_x) > 2.5)

            |

            (abs(z_scores_y) > 2.5)

        )

        # =====================================================
        # LABELS
        # =====================================================

        df_chart = df.copy()

        df_chart["Anomaly"] = anomaly_mask

        df_chart["Anomaly"] = df_chart[
            "Anomaly"
        ].map({

            True: "Anomaly",

            False: "Normal"

        })

        # =====================================================
        # SCATTER PLOT
        # =====================================================

        fig = px.scatter(

            df_chart,

            x=x_col,

            y=y_col,

            color="Anomaly",

            hover_data=df_chart.columns,

            title=f"🚨 Anomaly Detection: {x_col} vs {y_col}",

            height=500

        )

        # =====================================================
        # INTERACTIVE SETTINGS
        # =====================================================

        fig.update_traces(

            marker=dict(size=10),

            hovertemplate=

            "<b>%{x}</b><br>" +

            f"{x_col}: %{{x}}<br>" +

            f"{y_col}: %{{y}}<br>" +

            "<extra></extra>"

        )

        fig.update_layout(

            template="plotly_white",

            hovermode="closest"

        )

        # =====================================================
        # RETURN HTML
        # =====================================================

        return fig.to_html(

            full_html=False,

            include_plotlyjs="cdn"

        )

    except Exception:

        return None
