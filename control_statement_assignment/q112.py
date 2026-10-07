for i in range(5, 0, -1):
    for k in range(5-i):
        print(" ", end = "")
    for j in range(i):
        print(chr(ord('A') + j), end = "")
        
    print()

    
