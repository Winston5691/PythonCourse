# simple
for item in 'python':
    print(item) 

#List
for list in ['Cost of sales', 'salaries', 'ruinning cost', 'taxes']:
    print(list)
    
#numbers
for numbers in [1,2,3,4,5]:
    print(numbers)
    
    
#range
for numbers1 in range(10):
    print(numbers1)

for numbers2 in range(1, 10, 2):
    print (numbers2)
    
#Arithmetic

prices = [10,23, 25, 18, 15]
total = 0
for price in prices:
    total += price
    print(f"Total: {total}")