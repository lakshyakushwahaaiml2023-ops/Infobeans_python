arr1 = [1,2,3,5,6,9]
print(f"Array 1: {arr1}")
arr2 = [10,9,8,7,6,5,4]
print(f"Array 2: {arr2}")
arr3= []

i = 0
j = len(arr2) - 1

while i < len(arr1) and j >= 0:
    if arr1[i] < arr2[j]:
        arr3.append(arr1[i])
        i += 1
    else:
        arr3.append(arr2[j])
        j -= 1
while i < len(arr1):
    arr3.append(arr1[i])
    i += 1
while j >= 0:
    arr3.append(arr2[j])
    j -= 1
print(f"Merged array: {arr3}")