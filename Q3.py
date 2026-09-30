for i in range(10):
    for j in range(9,i,-1):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()
for i in range(8,0,-1):
    for j in range(9,i,-1):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()   