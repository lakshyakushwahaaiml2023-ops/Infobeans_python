for i in range(5, 0, -1):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i):
        if j== 0:
            print(j+1, end = "")
        elif i == 5:
            print(j+1, end = "")
        elif j == i-1:
            print(j+1, end = "")
        else:
            print("_", end = "")
        
    print()