a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Palindrome numbers between {a} and {b} are: ")
for i in range(min(a, b), max(a, b) + 1):
    temp = i
    sum = 0
    while temp != 0:
        rem = temp % 10
        temp //= 10 
        sum = sum * 10 + rem
    if sum == i:
        print(i, end = " ")       