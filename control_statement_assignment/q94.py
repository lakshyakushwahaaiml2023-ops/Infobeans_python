for i in range(5, 0, -1):
    for j in range(i):
        if i %2 != 0:
            print("*", end = "")
        else:
            print("#", end = "")
    print()