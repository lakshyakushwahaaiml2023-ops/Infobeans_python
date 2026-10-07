for i in range(5):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i+1):
        print(chr(ord('A') + j), end = " ")
    print()