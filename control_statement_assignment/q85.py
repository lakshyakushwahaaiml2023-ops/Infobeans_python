for i in range(5):
    for j in range(i+1):
        if i == j:
            if j % 2 == 0:
                print(1,end="")
            else:
                print(0,end="")
        elif j == 0:
            print(1,end="")
        elif i == 4:
            if j % 2 == 0:
                print(1,end="")
            else:
                print(0,end="")
        else:
            print(" ",end="")
    print()