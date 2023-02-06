names = ['Antony', 'Doe', 'Persie', 'Scholsey']
print(names[2])
print(names[2:])
print(names[1:3])
names[0] = 'Jeremy'
print(names)

#finding the largest number in a list
numbers = [10, 34, 56, 23, 45, 25, 67, 29,64]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print (max)
    