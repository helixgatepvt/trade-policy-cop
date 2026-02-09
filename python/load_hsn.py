import csv
from pathlib import Path

HSN_CSV = Path(__file__).parent.parent / "data" / "hsn" / "hsn_sample.csv"

def load_hsn():
    records = {}
    with open(HSN_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records[row["hsn"]] = row
    return records

if __name__ == "__main__":
    hsn_data = load_hsn()
    print(hsn_data.get("7318"))
