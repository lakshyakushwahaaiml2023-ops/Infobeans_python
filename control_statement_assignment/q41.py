a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

x = max(a, b)

while True:
    if x % a == 0 and x % b == 0:
        print(x)
        break
    x += 1