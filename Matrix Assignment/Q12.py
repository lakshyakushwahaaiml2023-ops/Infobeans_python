#Matrix Multiplication

m1 = [
    [1,2,3],
    [4,5,6]
] #==> 2x3 matrix

m2 = [
    [7,8],
    [9,10],
    [11,12]
] #==> 3x2 matrix


r1 = len(m1)
r2 = len(m2)
c1 = len(m1[0])
c2 = len(m2[0])

res_matrix = [[0]*c2 for _ in range(r1)]

for i in range(r1):
    for j in range(c2):
        for k in range(r2):
            res_matrix[i][j] += m1[i][k] * m2[k][j]

for i in res_matrix:
    print(i)