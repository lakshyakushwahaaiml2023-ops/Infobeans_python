for i in range(6):
    for k in range(5, i, -1):
        print(" ", end="")
    for j in range(i):
        if j == 0:
            print(chr(ord('A') + j), end = "")
        elif i == 5:
            print(chr(ord('A') + j), end = "")
        elif j == i-1:
            print(chr(ord('A') + j), end = "")
        else:
            print("_", end = "")
    print()