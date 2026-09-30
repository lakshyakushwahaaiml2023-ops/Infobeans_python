n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i):
        if i%2 == 0:
            print(0, end = "")
        else:
            print(1, end = "")
    print()