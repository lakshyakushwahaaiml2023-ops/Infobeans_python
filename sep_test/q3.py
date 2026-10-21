num = int(input("Enter a number: "))
temp = num

sum = 0
rev = 0
num_dig = 0
smallest = num%10
largest = num%10

while num != 0:
    rem = num %10
    sum += rem
    rev = rev*10 + rem
    num_dig += 1
    if rem < smallest:
        smallest = rem
    if rem > largest:
        largest = rem
    num = num // 10
print(f"Sum of digits: {sum}")
print(f"Number of digits: {num_dig}")
print(f"Largest digit: {largest}")
print(f"Smallest number: {smallest}")
print(f"Palindrome: Yes") if rev == temp else print("Palindrome: No")
