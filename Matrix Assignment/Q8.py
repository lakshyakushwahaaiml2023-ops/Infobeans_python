#Swapping maximum sum row with minimum sum row

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
print("Original Matrix : ")
for i in matrix:
    print(i)

max_sum = float('-inf')
min_sum = float('inf')
max_index = 0
min_index = 0


for i in range(len(matrix)):
    sum = 0
    for j in matrix[i]:
        sum += j
    if max_sum < sum:
        max_sum = sum
        max_index = i
    if min_sum > sum:
        min_sum = sum
        min_index = i
matrix[min_index], matrix[max_index] = matrix[max_index], matrix[min_index]
print("Matrix after swapping : ")
for i in matrix:
    print(i)        