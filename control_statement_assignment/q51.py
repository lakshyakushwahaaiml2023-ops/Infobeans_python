a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Reverse numbers between {a} and {b} are: ")
f = 0
if(max(a,b)%10 == 0):
    f = 1
for i in range(min(a, b), max(a, b) + 1):
    temp = i
    sum = 0
    while temp != 0:
        rem = temp % 10
        temp //= 10 
        sum = sum * 10 + rem 
    if(f == 1 and i == max(a,b)):
        print(0, end = "")
    print(sum, end = " ") 