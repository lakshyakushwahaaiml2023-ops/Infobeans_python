list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

list1=set(list1)
list2=set(list2)

common = set()
unique = set()

print("Common Elements: ", end = " ")
for i in list1:
    if i in list2:
        common.add(i)
print(common)


for i in list1:
    if i not in list2:
        unique.add(i)
for i in list2:
    if i not in list1:
        unique.add(i)

print("Unique Elemenets: ", unique)

