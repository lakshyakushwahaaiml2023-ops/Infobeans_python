for i in range(6):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i):
        if j == 0:
            print("1", end = "")
        elif i == 5:
            print(1, end = "")
        else:
            print("*", end = "")
    if i > 1 and i <= 5:
        for l in range(i-1):
            if l == i-2:
                print("1", end = "")
            elif i == 5:
                print(1, end = "")
            else:
                print("*", end = "")
    print()