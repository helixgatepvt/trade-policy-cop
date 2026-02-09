from load_hsn import lookup_hsn

def check_product(hsn_code: str):
    record = lookup_hsn(hsn_code)
    if not record:
        return "HSN not found. Manual review required."
    return (
        f"HSN {record['hsn']} identified: "
        f"{record['description']} (Chapter {record['chapter']})"
    )

if __name__ == "__main__":
    print(check_product("7318"))
