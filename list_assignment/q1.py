arr = [5]
if len(arr) > 1 and arr[0] > arr[1]:
    print(1)
elif arr[len(arr) - 1] > arr[len(arr) - 2]:
    print(1)
else:
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            print(1)
            break
    else:
        print(0)