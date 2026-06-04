import pandas as pd
import chardet


def detect_encoding(file_path):

    with open(file_path, "rb") as file:

        raw_data = file.read(100000)

    result = chardet.detect(raw_data)

    encoding = result["encoding"]

    return encoding


def read_file(file_path):

    try:

        # Detect encoding
        encoding = detect_encoding(file_path)

        print(f"📄 Detected Encoding: {encoding}")

        # Read CSV
        df = pd.read_csv(
            file_path,
            encoding=encoding
        )

        print("✅ CSV loaded successfully")

        return df

    except Exception as e:

        print(f"❌ Error reading file: {e}")