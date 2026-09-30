k = ord("A")
for i in range(10):
    if i % 2 == 1:
        for j in range(i):
            print(chr(k), end = "")
            k+= 1
        print()