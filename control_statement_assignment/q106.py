for i in range(6):
    for k in range(5, i, -1):
        print(" ", end="")
    for j in range(i):
        if j%2 == 0:
            print(1, end = "")
        else:
            print(0, end = "")
    print()