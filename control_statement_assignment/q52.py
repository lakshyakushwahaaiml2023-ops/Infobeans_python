a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
for i in range(min(a, b), max(a, b) + 1):
    dig_num = 0
    temp = i
    while temp != 0:
        temp = temp//10
        dig_num += 1
    sum = 0
    temp = i
    while temp != 0:
        rem = temp %10
        sum = sum + rem**dig_num
        temp = temp // 10
    if sum == i:
        print(i, end = " ")
     