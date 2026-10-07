for i in range(5, 0, -1):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i):
        if j == 0:
            print(i, end = "")
        elif i == 5:
            print(i, end = "")   
        elif j == i - 1:
            print(i, end = "") 
        else:
            print("_", end = "")
    print()