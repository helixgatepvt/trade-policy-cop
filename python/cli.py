import argparse
from load_hsn import lookup_hsn
from load_tariffs import lookup_mfn_tariff

TEXTILE_CHAPTERS = {"50","51","52","53","54","55","56","57","58","59","60","61","62","63"}

def determine_policy(export_country, import_country, chapter):
    if export_country == "IN" and import_country == "US" and chapter in TEXTILE_CHAPTERS:
        return "MFA"
    if export_country == "IN" and import_country in {"EU"}:
        return "FTA_CHECK"
    return "MFN"

def main():
    parser = argparse.ArgumentParser(description="Trade Policy COP CLI")
    parser.add_argument("--hsn", required=True)
    parser.add_argument("--export", required=True)
    parser.add_argument("--import_country", required=True)
    args = parser.parse_args()

    hsn_record = lookup_hsn(args.hsn)
    if not hsn_record:
        print("HSN not found. Manual review required.")
        return

    chapter = hsn_record["chapter"]
    policy = determine_policy(args.export, args.import_country, chapter)

    print("=== Trade Decision ===")
    print(f"HSN: {args.hsn}")
    print(f"Description: {hsn_record['description']}")
    print(f"Chapter: {chapter}")
    print(f"Applicable policy: {policy}")

    if policy == "MFN":
        tariff = lookup_mfn_tariff(args.hsn, args.import_country)
        print(f"Tariff context: {tariff['rate_note'] if tariff else 'MFN applies'}")

    print("\n=== Prompt-ready input ===")
    print(f"""
Export country: {args.export}
Import country: {args.import_country}
Product description: {hsn_record['description']}
HSN: {args.hsn}
Chapter: {chapter}
Applicable policy: {policy}
""")

if __name__ == "__main__":
    main()
