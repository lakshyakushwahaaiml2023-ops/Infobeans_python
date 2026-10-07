for i in range(6):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i):
        if j == 0:
            print(chr(ord('A') + i - 1), end = "")
        elif i == 5:
            print(chr(ord('A') + i - 1)*2, end = "")
        elif j == i-1:
            print(chr(ord('A') + i - 1), end = "")
        else:
            print(" ", end = "")
    print()