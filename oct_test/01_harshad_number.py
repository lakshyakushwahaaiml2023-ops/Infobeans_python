def harshad_num(num):
    digit_sum = 0
    temp = num
    while temp != 0:
        rem = temp %10
        digit_sum += rem
        temp = temp // 10
    return num % digit_sum == 0

num = int(input("Enter a number: "))
ans = harshad_num(num)
print(f"{num} is Harshad number") if ans else print(f"{num} is not a Harshad number")