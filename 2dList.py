matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)

#find a value in  the matrix
matrix[0][1]
#2
#change the value
matrix[0][1] = 20
print(matrix)

# get all items in the matrix a list
for row in matrix:
    for item in row:
        print(item)
