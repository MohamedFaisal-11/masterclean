def generate_report(

    df,

    warnings,

    profile,

    charts,

    ai_insights=None,

    anomalies=None,

    output_file="report.html"

):

    # =========================================================
    # EXTRACT RISK & QUALITY
    # =========================================================

    risk_score = "N/A"

    quality_grade = "N/A"

    if ai_insights:

        for insight in ai_insights:

            if "DATA RISK SCORE" in insight:

                risk_score = insight

            if "DATA QUALITY GRADE" in insight:

                quality_grade = insight

    # =========================================================
    # HTML START
    # =========================================================

    html = f"""

    <html>

    <head>

        <title>MasterClean AI Dashboard</title>

        <meta charset="UTF-8">

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <style>

            * {{

                box-sizing: border-box;

            }}

            body {{

                margin: 0;

                padding: 30px;

                font-family: Arial, sans-serif;

                background: #f4f6f9;

                color: #1f2937;

            }}

            h1, h2 {{

                margin-top: 0;

            }}

            .header {{

                margin-bottom: 30px;

            }}

            .header p {{

                color: #555;

                font-size: 18px;

            }}

            /* =========================================================
               KPI CARDS
            ========================================================= */

            .grid {{

                display: grid;

                grid-template-columns:
                    repeat(auto-fit, minmax(240px, 1fr));

                gap: 20px;

                margin-bottom: 30px;

            }}

            .kpi-card {{

                background: white;

                padding: 25px;

                border-radius: 14px;

                text-align: center;

                box-shadow:
                    0px 4px 10px rgba(0,0,0,0.08);

            }}

            .kpi-title {{

                font-size: 16px;

                color: #666;

                margin-bottom: 10px;

            }}

            .kpi-value {{

                font-size: 36px;

                font-weight: bold;

                color: #111827;

            }}

            /* =========================================================
               CARDS
            ========================================================= */

            .card {{

                background: white;

                border-radius: 16px;

                padding: 25px;

                margin-bottom: 30px;

                box-shadow:
                    0px 4px 12px rgba(0,0,0,0.08);

            }}

            /* =========================================================
               AI INSIGHTS
            ========================================================= */

            .insight {{

                background: #f9fafb;

                padding: 15px;

                border-left: 5px solid #3b82f6;

                border-radius: 8px;

                margin-bottom: 12px;

                line-height: 1.6;

                font-size: 16px;

            }}

            /* =========================================================
               WARNINGS
            ========================================================= */

            .warning {{

                color: #c0392b;

                font-weight: bold;

                margin-bottom: 12px;

                font-size: 17px;

            }}

            .success {{

                color: #27ae60;

                font-weight: bold;

                font-size: 17px;

            }}

            /* =========================================================
               TABLES
            ========================================================= */

            table {{

                width: 100%;

                border-collapse: collapse;

                margin-top: 15px;

            }}

            table, th, td {{

                border: 1px solid #e5e7eb;

            }}

            th, td {{

                padding: 14px;

                text-align: left;

            }}

            th {{

                background: #f3f4f6;

            }}

            /* =========================================================
               RISK BADGES
            ========================================================= */

            .risk-badge {{

                display: inline-block;

                padding: 12px 18px;

                background: #fdecea;

                color: #c0392b;

                border-radius: 10px;

                font-weight: bold;

                margin-bottom: 10px;

            }}

            .grade-badge {{

                display: inline-block;

                padding: 12px 18px;

                background: #eafaf1;

                color: #27ae60;

                border-radius: 10px;

                font-weight: bold;

            }}

            /* =========================================================
               ANOMALY BOXES
            ========================================================= */

            .anomaly-danger {{

                background: #fff0f0;

                color: #c0392b;

                padding: 15px;

                border-radius: 10px;

                margin-bottom: 12px;

                font-weight: bold;

            }}

            .anomaly-warning {{

                background: #fffbea;

                color: #f39c12;

                padding: 15px;

                border-radius: 10px;

                margin-bottom: 12px;

            }}

            .anomaly-summary {{

                background: #eef5ff;

                color: #2c3e50;

                padding: 15px;

                border-radius: 10px;

                margin-bottom: 12px;

            }}

            /* =========================================================
               CHART GRID
            ========================================================= */

            .chart-grid {{

                display: grid;

                grid-template-columns:
                    repeat(auto-fit, minmax(500px, 1fr));

                gap: 24px;

            }}

            .chart-box {{

                background: #ffffff;

                border-radius: 14px;

                padding: 15px;

                box-shadow:
                    0px 2px 8px rgba(0,0,0,0.08);

                overflow: hidden;

                min-height: 550px;

            }}

            .chart-box .plotly-graph-div {{

                width: 100% !important;

                height: 520px !important;

            }}

            /* =========================================================
               RESPONSIVE
            ========================================================= */

            @media(max-width: 768px) {{

                .chart-grid {{

                    grid-template-columns: 1fr;

                }}

            }}

        </style>

    </head>

    <body>

        <!-- =====================================================
             HEADER
        ====================================================== -->

        <div class="header">

            <h1>
                🚀 MasterClean AI Analytics Dashboard
            </h1>

            <p>
                Enterprise-grade AI-powered dataset auditing,
                validation, anomaly detection, and analytics platform.
            </p>

        </div>

        <!-- =====================================================
             KPI GRID
        ====================================================== -->

        <div class="grid">

            <div class="kpi-card">

                <div class="kpi-title">
                    Rows
                </div>

                <div class="kpi-value">
                    {profile['rows']}
                </div>

            </div>

            <div class="kpi-card">

                <div class="kpi-title">
                    Columns
                </div>

                <div class="kpi-value">
                    {profile['columns']}
                </div>

            </div>

            <div class="kpi-card">

                <div class="kpi-title">
                    Missing Values
                </div>

                <div class="kpi-value">
                    {profile['missing_values']}
                </div>

            </div>

            <div class="kpi-card">

                <div class="kpi-title">
                    Health Score
                </div>

                <div class="kpi-value">
                    {profile['health_score']}
                </div>

            </div>

        </div>

        <!-- =====================================================
             AI SUMMARY
        ====================================================== -->

        <div class="card">

            <h2>
                🧠 Executive AI Summary
            </h2>

    """

    # =========================================================
    # AI INSIGHTS
    # =========================================================

    if ai_insights:

        for insight in ai_insights:

            html += f"""

            <div class="insight">

                {insight}

            </div>

            """

    else:

        html += """

        <p class="success">

            ✅ No major AI insights generated.

        </p>

        """

    # =========================================================
    # RISK SECTION
    # =========================================================

    html += f"""

        </div>

        <div class="card">

            <h2>
                🚨 Risk & Quality Overview
            </h2>

            <div class="risk-badge">

                {risk_score}

            </div>

            <br><br>

            <div class="grade-badge">

                {quality_grade}

            </div>

        </div>

    """

    # =========================================================
    # ANOMALY SECTION
    # =========================================================

    html += """

        <div class="card">

            <h2>
                🚨 Anomaly Detection
            </h2>

    """

    if anomalies:

        for anomaly in anomalies:

            if "🚨" in anomaly:

                html += f"""

                <div class="anomaly-danger">

                    {anomaly}

                </div>

                """

            elif "💡" in anomaly:

                html += f"""

                <div class="anomaly-warning">

                    {anomaly}

                </div>

                """

            elif "🧠" in anomaly:

                html += f"""

                <div class="anomaly-summary">

                    {anomaly}

                </div>

                """

            else:

                html += f"""

                <p>{anomaly}</p>

                """

    else:

        html += """

        <p class="success">

            ✅ No anomalies detected.

        </p>

        """

    # =========================================================
    # VALIDATION WARNINGS
    # =========================================================

    html += """

        </div>

        <div class="card">

            <h2>
                ⚠ Validation Warnings
            </h2>

    """

    if warnings:

        for warning in warnings:

            html += f"""

            <p class="warning">

                {warning}

            </p>

            """

    else:

        html += """

        <p class="success">

            ✅ No major validation issues found.

        </p>

        """

    # =========================================================
    # DATATYPE SUMMARY
    # =========================================================

    html += """

        </div>

        <div class="card">

            <h2>
                🧠 Datatype Summary
            </h2>

            <table>

                <tr>

                    <th>Datatype</th>

                    <th>Count</th>

                </tr>

    """

    for dtype, count in profile["datatypes"].items():

        html += f"""

        <tr>

            <td>{dtype}</td>

            <td>{count}</td>

        </tr>

        """

    html += """

            </table>

        </div>

    """

    # =========================================================
    # CHARTS SECTION
    # =========================================================

    html += """

        <div class="card">

            <h2>
                📈 Interactive Visualizations
            </h2>

            <div class="chart-grid">

    """

    for chart in charts:

        html += f"""

            <div class="chart-box">

                {chart}

            </div>

        """

    html += """

            </div>

        </div>

    """

    # =========================================================
    # HTML END
    # =========================================================

    html += """

    </body>

    </html>

    """

    # =========================================================
    # SAVE REPORT
    # =========================================================

    with open(output_file, "w", encoding="utf-8") as file:

        file.write(html)

    print(f"✅ Unified dashboard generated as {output_file}")
