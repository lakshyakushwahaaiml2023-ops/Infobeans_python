#Left Diagonal
'''
[[00 , 01, 02, 03],
 [10, 11, 12, 13],
 [20, 21, 22, 23] ==> 03, 12, 21, 30
 [30, 31, 32, 33]
]
'''
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
a = 0
b = len(matrix)-1

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == a and j == b:
            print(matrix[i][j], end = " ")
            a+= 1
            b-=1
        else:
            print("_", end = " ")
    print()