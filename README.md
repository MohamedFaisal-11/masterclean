# MasterClean

MasterClean is an automated CSV cleaning toolkit for Python.

## Features

* CSV file reading
* Missing value handling
* Duplicate removal
* Column standardization
* Clean CSV export

---

## Installation

```bash
pip install masterclean
```

---

## Usage

```python
from masterclean import read_file, clean_data, export_data

df = read_file("sample.csv")

cleaned_df = clean_data(df)

export_data(cleaned_df)
```

---

## Example Output

```text
✅ CSV loaded successfully
✅ Data cleaned successfully
✅ Cleaned CSV exported as cleaned_data.csv
```

---

## Author

Mohamed Faisal Maraicar N
