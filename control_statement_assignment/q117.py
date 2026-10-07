for i in range(5):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i+1):
        if j == 0:
            print("X", end = " ")
        elif j == i:
            print("X", end = " ")
        elif i == 4:
            print("X", end = " ")
        else:
            print("_", end = "_")
    print()