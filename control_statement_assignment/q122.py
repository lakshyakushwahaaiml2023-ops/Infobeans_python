for i in range(5):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i+1):
        if j == 0:
            print(j+1, end = " ")
        elif j == i:
            print(1, end = " ")
        else:
            print(j+i, end = " ")
    print()