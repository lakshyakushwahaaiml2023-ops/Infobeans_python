n = int(input("Enter a number: "))
sum = n%10
while n!= 0:
    if(n < 10):
        sum += n
    n = n//10
print(f"Sum of first and last digit: {sum}")