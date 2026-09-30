a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Perfect numbers between {a} and {b} are: ")
for i in range(min(a, b), max(a, b) + 1):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i, end = " ")