for i in range(5):
    for j in range(5, i, -1):
        if i == 0:
            print("*", end = "")
        elif j == 5:
            print("*", end = "")
        elif j == i+1:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()