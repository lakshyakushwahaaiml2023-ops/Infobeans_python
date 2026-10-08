#Reversing all rows in the matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

for i in matrix:
    start = 0
    end = len(i) - 1
    while start  < end:
        i[start], i[end] = i[end], i[start]
        start += 1
        end -= 1
for i in matrix:
    print(i)