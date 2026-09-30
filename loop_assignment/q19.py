n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum += 1/i
    print(f"1/{i} + ", end = "")
print(f"Sum of series is: {sum}")