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

#Emoji converter
Greeting = input("Greet me: ")
words = Greeting.split(' ')
emoji = {
    ":)": "😂",
    ":(": "😑"
}
display = ""
for word in words:
    display += emoji.get(word, word) + " "
print(display)