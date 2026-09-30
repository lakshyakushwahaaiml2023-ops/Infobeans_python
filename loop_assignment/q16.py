n = int(input("Enter a multiple of three: "))
if n%3 != 0:
    print("The number is not a multiple of three.")

for i in range(-(n), n+1, 3):
    print(i, end = " ")