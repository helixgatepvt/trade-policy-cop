from load_hsn import lookup_hsn
from load_tariffs import lookup_mfn_tariff

def run_trade_check(hsn: str, country: str):
    hsn_record = lookup_hsn(hsn)
    if not hsn_record:
        return {
            "status": "manual_review",
            "reason": "HSN not found"
        }

    tariff_record = lookup_mfn_tariff(hsn, country)

    return {
        "hsn": hsn_record,
        "tariff": tariff_record,
        "prompt_input": {
            "product_description": hsn_record["description"],
            "chapter": hsn_record["chapter"],
            "tariff_note": tariff_record["rate_note"] if tariff_record else "No tariff record found"
        }
    }

if __name__ == "__main__":
    result = run_trade_check("7318", "US")
    print(result)
