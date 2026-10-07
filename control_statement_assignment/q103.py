for i in range(6):
    for k in range(5, i, -1):
        print(" ", end="")
    for j in range(i):
        print(chr(ord('A') + j), end = "")
    print()