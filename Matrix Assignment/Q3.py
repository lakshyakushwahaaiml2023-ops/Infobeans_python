matrix1 = [[1]*3 for _ in range(3)]
matrix2 = [[2]*3 for _ in range(3)]
matrix3 = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
        print(matrix3[i][j], end = " ")
    print()