shop = input("Product: ")
products = {
    "1": "Guinness",
    "2": "White cap",
    "3": "Pilsner",
    "4": "Tusker",
    "5": "Savannah"
}
output = ""
for ch in shop:
    output += products.get(ch, "!") + " "
print(output)