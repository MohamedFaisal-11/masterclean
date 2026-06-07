import os
import pandas as pd

from masterclean.dashboard.report import generate_report


def test_report_generation():

    df = pd.DataFrame({

        "name": ["John", "Alice"],
        "age": [25, 30]

    })

    profile = {

        "rows": 2,
        "columns": 2,
        "missing_values": 0,
        "duplicate_rows": 0,
        "memory_usage_mb": 0.01,
        "health_score": 100,
        "missing_summary": {},
        "datatypes": {
            "object": 1,
            "int64": 1
        }

    }

    generate_report(
        df=df,
        warnings=[],
        profile=profile,
        charts=[],
        ai_insights=[],
    )

    assert os.path.exists(
        "report.html"
    )
