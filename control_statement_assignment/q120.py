for i in range(6):
    x = 1
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i):
        print(chr(ord('A') + x-1), end = "")
        x+=1
    if i > 1:
        for l in range(i-1):
            print(chr(ord('A') + x-1), end = "")
            x+=1
    print()