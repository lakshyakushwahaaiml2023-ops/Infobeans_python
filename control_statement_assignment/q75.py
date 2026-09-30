for i in range(6):
    for j in range(i):
        if j == i-1 or j==0:
            print("*", end = "")
        elif(i == 5):
            print("*",end = "")
        else:
            print(" ", end = "")
    print()