l1 = [1,3,12,2,11,34,12,43,67,0]
for i in range(len(l1)-1):
    for j in range(len(l1) - i - 1):
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]
print(f"Sorted list: {l1}")
k = 4
print(f"{k}th largest element: {l1[-k]}")
print(f"{k}th smallest element: {l1[k-1]}")