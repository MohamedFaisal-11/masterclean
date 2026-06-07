import pandas as pd

from scipy.stats import zscore


def detect_anomalies(df):

    anomalies = []

    anomaly_summary = []

    # =====================================================
    # NUMERIC COLUMN DETECTION
    # =====================================================

    numeric_cols = df.select_dtypes(

        include="number"

    ).columns

    # =====================================================
    # Z-SCORE THRESHOLD
    # =====================================================

    threshold = 2.5

    # =====================================================
    # ANOMALY DETECTION LOOP
    # =====================================================

    for col in numeric_cols:

        try:

            # ---------------------------------------------
            # CLEAN SERIES
            # ---------------------------------------------

            clean_series = df[col].dropna()

            # Skip small columns
            if len(clean_series) < 5:

                continue

            # Skip constant columns
            if clean_series.nunique() <= 1:

                continue

            # ---------------------------------------------
            # Z-SCORE CALCULATION
            # ---------------------------------------------

            z_scores = zscore(clean_series)

            # ---------------------------------------------
            # DETECT OUTLIERS
            # ---------------------------------------------

            outlier_mask = abs(z_scores) > threshold

            outlier_count = outlier_mask.sum()

            outlier_percentage = (

                outlier_count / len(clean_series)

            ) * 100

            # ---------------------------------------------
            # ANOMALY FOUND
            # ---------------------------------------------

            if outlier_count >= 1:

                anomalies.append(

                    f"🚨 '{col}' contains "

                    f"{outlier_count} anomalies "

                    f"({outlier_percentage:.1f}%)."

                )

                # =====================================================
                # CONTEXT-AWARE INSIGHTS
                # =====================================================

                if "salary" in col.lower():

                    anomalies.append(

                        "💡 Possible payroll anomaly detected."

                    )

                elif "sales" in col.lower():

                    anomalies.append(

                        "💡 Abnormal sales spike detected."

                    )

                elif "transaction" in col.lower():

                    anomalies.append(

                        "💡 Suspicious transaction behavior detected."

                    )

                elif "age" in col.lower():

                    anomalies.append(

                        "💡 Unusual demographic values detected."

                    )

                elif "price" in col.lower():

                    anomalies.append(

                        "💡 Pricing irregularities detected."

                    )

                else:

                    anomalies.append(

                        "💡 Review unusual values carefully."

                    )

                anomaly_summary.append(

                    f"{outlier_count} anomalies in '{col}'"

                )

        except Exception:

            pass

    # =====================================================
    # FINAL SUMMARY
    # =====================================================

    if anomaly_summary:

        summary = (

            "🧠 Anomaly Summary: "

            + ", ".join(anomaly_summary[:5])

            + "."

        )

        anomalies.insert(0, summary)

    else:

        anomalies.append(

            "✅ No major anomalies detected."

        )

    # =====================================================
    # CONSOLE OUTPUT
    # =====================================================

    print("\nANOMALY DETECTION")

    print("=" * 40)

    for item in anomalies:

        print(item)

    return anomalies
