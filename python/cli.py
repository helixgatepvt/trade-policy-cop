import argparse
from load_hsn import lookup_hsn
from load_tariffs import lookup_mfn_tariff

def main():
    parser = argparse.ArgumentParser(description="Trade Policy COP CLI")
    parser.add_argument("--hsn", required=True, help="HSN code")
    parser.add_argument("--country", required=True, help="Import country code (US, IN, EU)")
    args = parser.parse_args()

    hsn = args.hsn
    country = args.country

    hsn_record = lookup_hsn(hsn)
    if not hsn_record:
        print("HSN not found. Manual review required.")
        return

    tariff_record = lookup_mfn_tariff(hsn, country)

    print("=== Trade Check Result ===")
    print(f"HSN: {hsn}")
    print(f"Description: {hsn_record['description']}")
    print(f"Chapter: {hsn_record['chapter']}")

    if tariff_record:
        print(f"Tariff note: {tariff_record['rate_note']}")
    else:
        print("Tariff note: No MFN tariff record found")

    print("\n=== Prompt-ready input ===")
    print(f"""
Product description: {hsn_record['description']}
HSN: {hsn}
Chapter: {hsn_record['chapter']}
Tariff context: {tariff_record['rate_note'] if tariff_record else 'Unknown'}
""")

if __name__ == "__main__":
    main()
