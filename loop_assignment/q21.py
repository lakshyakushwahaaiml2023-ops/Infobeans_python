n = int(input("Enter a number: "))
for i in range(n+1):
    if(i == n):
        print(i**2, end = " ")
    else:
        print(i**2, end = ", ")