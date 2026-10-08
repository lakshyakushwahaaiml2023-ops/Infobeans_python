#Even odd element sum

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

even_sum = 0
odd_sum = 0

for i in matrix:
    for j in i:
        if j%2 == 0:
            even_sum += j
        else:
            odd_sum += j
print(f"Even elements sum : {even_sum}")
print(f"Odd elements sum: {odd_sum}")