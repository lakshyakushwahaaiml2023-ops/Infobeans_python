n = 123456
j = 1
while n !=0:    
    if j == 0:
        print(str(n)[::-1])
        j = 1
    else:
        print(n)
        j = 0
    n = n//10

