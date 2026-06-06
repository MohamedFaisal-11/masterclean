import pandas as pd
import chardet
from pathlib import Path


def detect_encoding(file_path):

    with open(file_path, "rb") as file:

        raw_data = file.read(100000)

    result = chardet.detect(raw_data)

    return result["encoding"]


def read_file(file_path):

    try:

        file_extension = Path(file_path).suffix.lower()

        # -----------------------------------
        # CSV Support
        # -----------------------------------

        if file_extension == ".csv":

            encoding = detect_encoding(file_path)

            print(f"📄 Detected Encoding: {encoding}")

            df = pd.read_csv(
                file_path,
                encoding=encoding
            )

            print("✅ CSV loaded successfully")

            return df

        # -----------------------------------
        # Excel Support
        # -----------------------------------

        elif file_extension in [".xlsx", ".xls"]:

            df = pd.read_excel(file_path)

            print("✅ Excel file loaded successfully")

            return df

        # -----------------------------------
        # Unsupported Files
        # -----------------------------------

        else:

            raise ValueError(
                f"Unsupported file format: {file_extension}\n"
                "Supported formats: .csv, .xlsx, .xls"
            )

    except FileNotFoundError:

        print("❌ File not found")

    except pd.errors.EmptyDataError:

        print("❌ File is empty")

    except Exception as e:

        print(f"❌ Error reading file: {e}")
