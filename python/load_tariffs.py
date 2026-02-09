import csv
from pathlib import Path

TARIFF_CSV = Path(__file__).parent.parent / "data" / "tariffs" / "mfn_sample.csv"

def load_tariffs():
    records = []
    with open(TARIFF_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records

def lookup_mfn_tariff(hsn: str, country: str):
    tariffs = load_tariffs()
    for row in tariffs:
        if row["hsn"] == hsn and row["country"] == country:
            return row
    return None

if __name__ == "__main__":
    print(lookup_mfn_tariff("7318", "US"))
