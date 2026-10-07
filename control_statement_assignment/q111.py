for i in range(5, 0, -1):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i):
        if j == 0:
            print(chr(ord('A') + j), end = "")
        elif i == 5:
            print(chr(ord('A') + j), end = "")   
        elif j == i - 1:
            print(chr(ord('A') + j), end = "") 
        else:
            print("_", end = "")
        
    print()

    
