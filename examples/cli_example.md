# CLI Example

## Run MasterClean

```bash
masterclean clean examples/sample.csv
```

---

## Expected Output

```text
📄 Detected Encoding: utf-8

✅ CSV loaded successfully
✅ Data cleaned successfully
✅ Datatypes optimized
✅ Data profile generated
✅ Unified interactive charts generated

VALIDATION WARNINGS
========================================
⚠ Negative values found in 'age'
⚠ Possible outliers detected in 'salary'

✅ Unified dashboard generated as report.html
✅ Cleaned CSV exported as cleaned_data.csv

🎉 Cleaning completed successfully
```

---

## Generated Files

* cleaned_data.csv
* report.html
