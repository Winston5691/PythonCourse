try:
    Age = int(input("Enter you age: "))
    print(Age)
except ValueError:
    print('invalid entry')