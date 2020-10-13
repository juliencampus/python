def totals(price, taxrate, qty):
    return {"price": (price * 1 + (taxrate/100)) * qty,"taxes": (taxrate/100)*price*qty}

def process_stock(name,totalprice,totaltaxes):
    discount = ""
    if totalprice > 1000:
        discount = f"- remise de {round(totalprice * 0.12,2)} €"
        price = totalprice * 0.88
    return f"Le total TTC du stock de {name}s est de {round(price,2)}€ (dont taxes de {round(totaltaxes,2)}€ {discount})"

if __name__ == '__main__':
    data = {
        "name": input('name:'),
        "price": float(input('price:')),
        "rate": round(float(input("tax rate:"))),
        "stock": int(input('stock:'))
    }
    totals = totals(data["price"], data["rate"], data["stock"])
    print(process_stock(data["name"],totals["price"],totals["taxes"]))



