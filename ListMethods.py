numbers= [22, 19, 28, 24, 22, 47, 67, 28]
# Adding numbers to the list
numbers.append(20) # adds to the last part
#adds 23 to after 19
numbers.insert(1,23)
#To arrange or sort in order
numbers.sort()
#T9 arrange or sort starting from the largest
numbers.reverse()
#copying a list
numbers2=numbers.copy()
#Removing duplicates
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
#Checking the existence of a number in the list
print(19 in numbers)
#counting characters in the list
print(numbers.count(28))
#removing an item-removes the value 28
numbers.remove(28) 
#To delete the last number in the list
numbers.pop()
#To delete everything
numbers.clear()