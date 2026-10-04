arr1 = [1, 2, 3, 4, 5]
arr2 = [1,2,3, 6, 7, 8, 9, 10]

print(f"First array: {arr1}")
print(f"Second array: {arr2}")
union = []

for i in arr1:
    if i not in union:
        union.append(i)

for i in arr2:
    if i not in union:
        union.append(i)

print(f"Union of the two arrays: {union}")

inter = []
for i in arr1:
    if i not in inter and i in arr2:
        inter.append(i)
print(f"Intersection of the two arrays: {inter}")
