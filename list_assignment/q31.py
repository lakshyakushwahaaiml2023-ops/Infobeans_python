arr1 = [3,2,1,7,6,3]
print(f"Array 1: {arr1}")
arr2 = [9,3,5,6,2,8,10]
print(f"Array 2: {arr2}")
arr3 = []

# for i in arr1:
#     if i % 2 == 0:
#         arr3.append(i)
# for i in arr2:
#     if i % 2 == 0:
#         arr3.append(i)
# for i in arr2:
#     if i % 2 != 0:
#         arr3.append(i)
# for i in arr1:
#     if i % 2 != 0:
#         arr3.append(i)

for i in arr1:
    if i % 2 != 0:
        arr3.insert(0, i)
for i in arr2:
    if i % 2 != 0:
        arr3.insert(0, i)
for i in range(len(arr2)-1, 0, -1):
    if arr2[i] % 2 == 0:
        arr3.insert(0, arr2[i])
for i in range(len(arr1)-1, 0, -1):
    if arr1[i] % 2 == 0:
        arr3.insert(0, arr1[i])

print(f"Merged Array: {arr3}")