# MasterClean

MasterClean is an automated CSV cleaning, preprocessing, and validation toolkit built with Python.

It helps users clean messy datasets with a single command-line instruction.

---

# Features

* Automatic CSV cleaning
* Missing value handling
* Duplicate removal
* Column standardization
* Datatype optimization
* Automatic encoding detection
* Validation engine
* Outlier detection
* Report generation
* Command Line Interface (CLI)
* Automated testing with pytest

---

# Installation

```bash
pip install masterclean
```

---

# Usage

## Command Line Usage

```bash
masterclean data.csv
```

MasterClean automatically:

* Reads CSV files
* Cleans missing values
* Removes duplicates
* Optimizes datatypes
* Detects validation issues
* Generates reports
* Exports cleaned datasets

---

## Python Usage

```python
from masterclean import (
    read_file,
    clean_data,
    optimize_dtypes,
    validate_data,
    generate_report,
    export_data
)

df = read_file("sample.csv")

df = clean_data(df)

df = optimize_dtypes(df)

validate_data(df)

generate_report(df)

export_data(df)
```

---

# Example Validation Output

```text
VALIDATION WARNINGS
========================================
⚠ Negative values found in 'age' (1 rows)
⚠ Possible outliers detected in 'salary' (1 rows)
⚠ Invalid boolean-like values found in 'active': {'maybe'}
```

---

# Project Structure

```text
masterclean/
├── cleaner.py
├── validator.py
├── datatypes.py
├── report.py
├── exporter.py
├── reader.py
├── cli.py
```

---

# Current Capabilities

* CSV preprocessing
* Data quality validation
* Encoding-aware file loading
* Automated reporting
* CLI-based automation

---

# Roadmap

Future improvements planned:

* Excel support
* HTML reports
* AI-powered cleaning suggestions
* Advanced schema validation
* Real-time dashboard integration

---

# Testing

Run tests using:

```bash
python -m pytest
```

---

# Author

Mohamed Faisal Maraicar N

GitHub:
https://github.com/MohamedFaisal-11
