'''
Maximum row sum
'''

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
max_sum = float('-inf')
for i in matrix:
    sum = 0
    for j in i:
        sum += j
    if max_sum < sum:
        max_sum = sum

print(f"Maximum sum : {max_sum}")
