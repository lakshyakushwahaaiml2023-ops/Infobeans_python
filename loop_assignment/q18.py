n = int(input("Enter a number: "))
a = 1
b = 2
print(f"{a} {b}", end = " ")
for i in range(n+1):
    c = a*b
    print(c, end = " ")
    a, b = b, c