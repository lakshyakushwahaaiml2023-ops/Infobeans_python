arr = [1,2,3,4,5]
maxi = arr[0]
low = arr[0]
for i in arr:
    if i > maxi:
        maxi = i
    if i < low:
        low = i
print(f"Maximum: {maxi} and Minimum: {low}")