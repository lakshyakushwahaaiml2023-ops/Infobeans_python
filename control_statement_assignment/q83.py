n = 5
for i in range(n):
    for j in range(n, n - i -1, -1):
        print(j, end = "")
    print()