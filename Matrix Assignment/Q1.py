#Sum of all elements of the matrix
row = 4
col = 4
matrix = [[3]*col for _ in range(row)]
sum = 0
for i in matrix:
    for j in i:
        print(j, end = " ")
        sum += j
    print()
print(f"Sum of all elements: {sum}")