arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(f"First array: {arr1}")
print(f"Second array: {arr2}")  
print(f"Third array: {arr3}")

for i in arr1:
    if i in set(arr2) and set(arr3):
        print(f"{i}", end = " ")