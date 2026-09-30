a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

for i in range(min(a, b), max(a, b) + 1):
    print(f"Factors of {i} are: ", end = "")
    for j in range(1, i+1):
        if i%j == 0:
            print(j, end = " ")
    print()