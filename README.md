# 🚀 MasterClean

![PyPI](https://img.shields.io/pypi/v/masterclean)

![Python](https://img.shields.io/badge/python-3.10+-blue)

![License](https://img.shields.io/badge/license-MIT-green)

Enterprise AI-powered Data Cleaning, Validation, Anomaly Detection & Analytics Toolkit for Python.

MasterClean automates:

- data cleaning
- preprocessing
- validation
- profiling
- anomaly detection
- AI insights
- visualization
- reporting
- analytics

using powerful CLI commands and Python APIs.

Designed for:

- Data Analysts
- Data Scientists
- ML Engineers
- Researchers
- Students
- Automation Workflows

---

# ✨ Features

# 🧹 Advanced Data Cleaning

- Missing value handling
- Duplicate row removal
- Empty string cleanup
- Whitespace cleanup
- Column standardization
- Datetime conversion
- Smart categorical filling
- Automatic preprocessing pipeline

---

# ⚡ Datatype Optimization

- Integer optimization
- Float optimization
- Boolean conversion
- Category optimization
- Datetime detection
- Memory usage reduction

---

# 🛡 Advanced Validation Engine

- Negative value detection
- Invalid boolean detection
- Email validation
- Phone validation
- Duplicate percentage warnings
- Missing value percentage analysis
- Mixed datatype detection

---

# 🚨 AI-Powered Anomaly Detection

- Z-score anomaly detection
- Salary anomaly detection
- Sales spike detection
- Demographic anomaly detection
- Interactive anomaly visualization
- Enterprise anomaly summaries

---

# 🧠 AI Insights Engine

- Dataset risk scoring
- Dataset quality grading
- Cardinality detection
- Identifier column detection
- Correlation intelligence
- ML readiness recommendations
- Automated contextual suggestions

---

# 📊 Advanced Profiling

- Dataset health score
- Missing value summaries
- Datatype analytics
- Memory usage analysis
- Numeric statistics
- Categorical summaries
- Dataset overview metrics

---

# 📈 Interactive Visualization Engine

- Plotly dashboards
- Histograms
- Boxplots
- Pie charts
- Correlation heatmaps
- Missing value charts
- Line charts
- Interactive anomaly scatter plots

---

# 📄 Reporting System

- Unified HTML analytics dashboard
- Validation summaries
- AI insight cards
- Risk overview cards
- Interactive visualizations
- Automated report generation

---

# 🖥 Professional CLI Toolkit

MasterClean supports multiple enterprise commands.

---

# 🚀 Full Automated Pipeline

```bash
masterclean clean data.csv
````

Runs:

* cleaning
* optimization
* anomaly detection
* validation
* profiling
* visualization
* AI analysis
* reporting
* exporting

---

# 🛡 Validation Only

```bash
masterclean validate data.csv
```

---

# 📊 Dataset Profiling

```bash
masterclean profile data.csv
```

---

# 📈 Dashboard Generation

```bash
masterclean dashboard data.csv
```

---

# 🚨 Anomaly Detection

```bash
masterclean anomaly data.csv
```

---

# 🔖 Show Version

```bash
masterclean version
```

---

# 📦 Installation

## Install from PyPI

```bash
pip install masterclean
```

---

# ⬆ Upgrade to Latest Version

```bash
pip install --upgrade masterclean
```

---

# 🐍 Python Usage

```python
from masterclean import *

# =====================================================
# READ DATASET
# =====================================================

df, file_extension = read_file(

    "data.csv"

)

# =====================================================
# CLEAN DATA
# =====================================================

df = clean_data(df)

# =====================================================
# OPTIMIZE DATATYPES
# =====================================================

df = optimize_dtypes(df)

# =====================================================
# VALIDATE DATA
# =====================================================

warnings = validate_data(df)

# =====================================================
# GENERATE PROFILE
# =====================================================

profile = generate_profile(df)

# =====================================================
# GENERATE VISUALIZATIONS
# =====================================================

charts = generate_charts(df)

# =====================================================
# AI INSIGHTS
# =====================================================

ai_insights = generate_ai_insights(df)

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
# GENERATE ENTERPRISE DASHBOARD
# =====================================================

generate_report(

    df=df,

    warnings=warnings,

    profile=profile,

    charts=charts,

    ai_insights=ai_insights,

    anomalies=anomalies,

    output_file="report.html"

)

# =====================================================
# EXPORT CLEANED DATA
# =====================================================

export_data(

    df,

    "cleaned_data",

    file_extension

)

print(

    "🚀 MasterClean pipeline completed successfully"

)
```


---

# 📂 Supported File Formats

| Format | Supported |
| ------ | --------- |
| CSV    | ✅         |
| XLSX   | ✅         |
| XLS    | ✅         |

---

# 🔄 Same-Format Export System

MasterClean automatically preserves output format.

| Input | Output            |
| ----- | ----------------- |
| CSV   | cleaned_data.csv  |
| XLSX  | cleaned_data.xlsx |
| XLS   | cleaned_data.xlsx |

---

# 📊 Example Validation Output

```text
VALIDATION WARNINGS
========================================

⚠ Negative values found in 'salary' (3 rows)

⚠ Invalid email values found in 'email' (5 rows)

⚠ High duplicate rows detected (14.2%)

⚠ Mixed datatypes detected in 'age'
```

---

# 🚨 Example Anomaly Output

```text
ANOMALY DETECTION
========================================

🧠 Anomaly Summary:
3 anomalies in 'salary',
2 anomalies in 'sales'.

🚨 'salary' contains 3 anomalies.
💡 Possible payroll anomaly detected.

🚨 'sales' contains 2 anomalies.
💡 Abnormal sales spike detected.
```

---

# 🏗 Enterprise Architecture

```text
Read
   ↓
Clean
   ↓
Optimize
   ↓
Detect Anomalies
   ↓
Validate
   ↓
Profile
   ↓
Generate AI Insights
   ↓
Visualize
   ↓
Generate Dashboard
   ↓
Export
```

---


# 📁 Project Structure

```text
masterclean/
│
├── preprocessing/
├── validation/
├── profiling/
├── visualization/
├── ml/
├── reports/
├── cli.py
├── __init__.py
│
tests/
│
README.md
pyproject.toml
requirements.txt
LICENSE
```

---

# 🧪 Testing

Run tests using:

```bash
python -m pytest
```

---

# 🔄 CI/CD

MasterClean uses GitHub Actions for:

* automated testing
* dependency validation
* continuous integration

---

# 🛣 Roadmap

Future improvements planned:

* Streamlit dashboard
* FastAPI integration
* AutoML recommendations
* Schema validation engine
* Large dataset optimization
* Cloud deployment support
* Plugin architecture
* Real-time analytics dashboards

---

# 🤝 Contributing

Contributions are welcome.

You can:

* report bugs
* suggest features
* improve documentation
* submit pull requests

---

# 📄 License

MIT License

---

# 👨‍💻 Author

Mohamed Faisal Maraicar N

GitHub:

https://github.com/MohamedFaisal-11/masterclean

