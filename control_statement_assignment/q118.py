for i in range(6):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i):
        if j == 0:
            print("*", end = "")
        else:
            print("*"*2, end = "")
    print()
