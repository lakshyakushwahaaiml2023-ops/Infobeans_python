for i in range(5, 0, -1):
    for j in range(i):
        if i == 5:
            print(i, end = "")
        elif j == 0:
            print(i, end = "")
        elif j == i-1:
            print(i, end = "")
        else:
            print(" ", end = "")
    print()