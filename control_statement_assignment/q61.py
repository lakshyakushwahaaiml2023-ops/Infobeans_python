y1 = int(input("Enter the first year: "))
y2 = int(input("Enter the second year: "))

for i in range(y1, y2 + 1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i, end = " ")