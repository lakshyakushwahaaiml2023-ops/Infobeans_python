k = ord('a')
for i in range(7):
    for j in range(0,i):
        if j == i-1 or j==0:
            print(chr(k), end = "")
            k+=1
        elif(i == 6):
            print(chr(k),end = "")
            k+=1
        else:
            print(" ", end = "")
    print()