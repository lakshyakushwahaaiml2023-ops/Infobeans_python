n = int(input("Enter the number: "))
sum = 0
while n != 0:
    rem = n % 10
    fact = 1
    for  i in range(2, rem+1):
        fact *= i
    sum += fact
    n = n // 10
if sum == fact:
    print("Strong Number")
else:
    print("Not a Strong Number")