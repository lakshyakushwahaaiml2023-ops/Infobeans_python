for i in range(6):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i):
        if j == 0:
            print("*", end = "")
        elif i == 5:
            print("*", end = "")
        else:
            print("_", end = "")
    if i > 1 and i <= 5:
        for l in range(i-1):
            if l == i-2:
                print("*", end = "")
            elif i == 5:
                print("*", end = "")
            else:
                print("_", end = "")
    
    print()