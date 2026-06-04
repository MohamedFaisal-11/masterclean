import pandas as pd


def generate_report(

    df,
    warnings=None,
    profile=None,
    charts="",
    output_file="report.html"

):

    rows = df.shape[0]
    columns = df.shape[1]

    missing_values = df.isnull().sum()

    dtypes = df.dtypes

    html = f"""
    <html>

    <head>

        <title>MasterClean Report</title>

        <style>

            body {{
                font-family: Arial;
                margin: 40px;
                background-color: #111827;
                color: white;
            }}

            h1 {{
                color: #00E5FF;
            }}

            h2 {{
                color: #A5F3FC;
                margin-top: 40px;
            }}

            table {{
                border-collapse: collapse;
                width: 95%;
                margin-bottom: 30px;
                background-color: #1F2937;
            }}

            th, td {{
                border: 1px solid #374151;
                padding: 12px;
                text-align: left;
            }}

            th {{
                background-color: #06B6D4;
                color: white;
            }}

            tr:nth-child(even) {{
                background-color: #111827;
            }}

            .warning {{
                color: #FCA5A5;
                font-weight: bold;
            }}

            .section {{
                margin-bottom: 50px;
            }}

        </style>

    </head>

    <body>

        <h1>🚀 MasterClean Analytics Dashboard</h1>

        <div class="section">

        <h2>Dataset Summary</h2>

        <table>

            <tr>
                <th>Metric</th>
                <th>Value</th>
            </tr>

            <tr>
                <td>Rows</td>
                <td>{rows}</td>
            </tr>

            <tr>
                <td>Columns</td>
                <td>{columns}</td>
            </tr>
    """

    # -----------------------------------
    # Profile Summary
    # -----------------------------------

    if profile:

        html += f"""

            <tr>
                <td>Duplicate Rows</td>
                <td>{profile.get("duplicate_rows", 0)}</td>
            </tr>

            <tr>
                <td>Memory Usage (MB)</td>
                <td>{profile.get("memory_usage_mb", 0)}</td>
            </tr>

        """

    html += """
        </table>

        </div>

        <div class="section">

        <h2>Column Types</h2>

        <table>

            <tr>
                <th>Column</th>
                <th>Datatype</th>
            </tr>
    """

    for col, dtype in dtypes.items():

        html += f"""
            <tr>
                <td>{col}</td>
                <td>{dtype}</td>
            </tr>
        """

    html += """
        </table>

        </div>

        <div class="section">

        <h2>Missing Values</h2>

        <table>

            <tr>
                <th>Column</th>
                <th>Missing Values</th>
            </tr>
    """

    for col, value in missing_values.items():

        html += f"""
            <tr>
                <td>{col}</td>
                <td>{value}</td>
            </tr>
        """

    html += """
        </table>

        </div>
    """

    # -----------------------------------
    # Numeric Statistics
    # -----------------------------------

    if profile:

        html += """
        <div class="section">

        <h2>Numeric Statistics</h2>

        <table>

            <tr>
                <th>Column</th>
                <th>Mean</th>
                <th>Median</th>
                <th>Min</th>
                <th>Max</th>
                <th>Std</th>
            </tr>
        """

        for col, stats in profile["column_profiles"].items():

            if "mean" in stats:

                html += f"""
                <tr>
                    <td>{col}</td>
                    <td>{stats.get("mean", "N/A")}</td>
                    <td>{stats.get("median", "N/A")}</td>
                    <td>{stats.get("min", "N/A")}</td>
                    <td>{stats.get("max", "N/A")}</td>
                    <td>{stats.get("std", "N/A")}</td>
                </tr>
                """

        html += """
        </table>

        </div>
        """

    # -----------------------------------
    # Categorical Statistics
    # -----------------------------------

    if profile:

        html += """
        <div class="section">

        <h2>Categorical Statistics</h2>

        <table>

            <tr>
                <th>Column</th>
                <th>Top Value</th>
                <th>Frequency</th>
                <th>Unique Values</th>
            </tr>
        """

        for col, stats in profile["column_profiles"].items():

            if "top_value" in stats:

                html += f"""
                <tr>
                    <td>{col}</td>
                    <td>{stats.get("top_value", "N/A")}</td>
                    <td>{stats.get("top_frequency", "N/A")}</td>
                    <td>{stats.get("unique_values", "N/A")}</td>
                </tr>
                """

        html += """
        </table>

        </div>
        """

    # -----------------------------------
    # Validation Warnings
    # -----------------------------------

    if warnings:

        html += """
        <div class="section">

        <h2 class="warning">
            ⚠ Validation Warnings
        </h2>

        <table>

            <tr>
                <th>Warning</th>
            </tr>
        """

        for warning in warnings:

            html += f"""
            <tr>
                <td>{warning}</td>
            </tr>
            """

        html += """
        </table>

        </div>
        """

    # -----------------------------------
    # Interactive Charts
    # -----------------------------------

    if charts:

        html += """
        <div class="section">

        <h2>📊 Interactive Visual Analytics</h2>
        """

        html += charts

        html += """
        </div>
        """

    html += """

    </body>

    </html>
    """

    with open(output_file, "w") as file:

        file.write(html)

    print(f"✅ Unified dashboard generated as {output_file}")