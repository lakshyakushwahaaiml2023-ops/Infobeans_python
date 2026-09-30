for i in range(5):
    for j in range(i+1):
        if j%2== 0:
            print("*", end = "")
        else:
            print("#", end = "")
    print()