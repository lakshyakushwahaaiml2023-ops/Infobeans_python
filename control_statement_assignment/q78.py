for i in range(6):
    for j in range(0,i):
        if j == i-1 or j==0:
            print(chr(ord('A')+j), end = "")
        elif(i == 5):
            print(chr(ord('A')+j),end = "")
        else:
            print(" ", end = "")
    print()