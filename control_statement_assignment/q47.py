a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
for i in range(min(a, b), max(a, b)):
    print(f"Table of {i} is: ")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")