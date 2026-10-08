'''Lower Triangular Matrix
[[00 , 01, 02],
 [10, 11, 12],
 [20, 21, 22] ==> 10, 20, 21
]

'''
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i > j:
            print(matrix[i][i], end = " ")
        else:
            print("_", end = " ")
    print()