from fastapi import FastAPI
from .load_hsn import lookup_hsn
from .load_tariffs import lookup_mfn_tariff


TEXTILE_CHAPTERS = {"50","51","52","53","54","55","56","57","58","59","60","61","62","63"}

app = FastAPI(title="Trade Policy COP API")

def determine_policy(export_country, import_country, chapter):
    if export_country == "IN" and import_country == "US" and chapter in TEXTILE_CHAPTERS:
        return "MFA"
    if export_country == "IN" and import_country == "EU":
        return "FTA_CHECK"
    return "MFN"

@app.post("/trade-check")
def trade_check(hsn: str, export: str, import_country: str):
    hsn_record = lookup_hsn(hsn)
    if not hsn_record:
        return {"status": "manual_review", "reason": "HSN not found"}

    chapter = hsn_record["chapter"]
    policy = determine_policy(export, import_country, chapter)

    response = {
        "hsn": hsn,
        "description": hsn_record["description"],
        "chapter": chapter,
        "export": export,
        "import_country": import_country,
        "policy": policy
    }

    if policy == "MFN":
        tariff = lookup_mfn_tariff(hsn, import_country)
        response["tariff_note"] = tariff["rate_note"] if tariff else "MFN applies"

    return response
