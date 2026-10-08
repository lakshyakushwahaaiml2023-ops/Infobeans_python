#Transpose of a matrix

row = 3
col = 3
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

res_matrix = [[0]* row for _ in range(col)]

for i in range(len(res_matrix)):
    for j in range(len(res_matrix[i])):
        res_matrix[i][j] = matrix[j][i]

        
print("Transpose Matrix: ")
for i in res_matrix:
    print(i)