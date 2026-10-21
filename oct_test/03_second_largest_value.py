def sec_max(arr):
    maxi = arr[0]
    s_max = float('-inf')
    for i in arr:
        if i > maxi:
            s_max = maxi
            maxi = i
        elif i < maxi and i > s_max:
            s_max = i
    return s_max
arr1 = [12, 45, 7, 45, 30, 22, 30]
print(sec_max(arr1))