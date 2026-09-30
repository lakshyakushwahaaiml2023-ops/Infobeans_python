l1 = [1,2,3,4,5,6,7,80,9,19]
min_ele = l1[0]
max_ele = l1[0]
for i in l1:
    if i < min_ele:
        min_ele = i
    if i > max_ele:
        max_ele = i
print("Minimum element:", min_ele)
print("Maximum element:", max_ele)