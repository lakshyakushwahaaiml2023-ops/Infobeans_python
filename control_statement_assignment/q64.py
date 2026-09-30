n = int(input("Enter a number: "))
for i in range(n):
    for j in range(0,i):
        if j == i-1:
            print("*", end = "")
        else:
            print(" ",end = "")
    print()