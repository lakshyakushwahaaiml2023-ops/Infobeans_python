arr = [9, 4, -2, -1, 5, 0, -5, -3, -2]
print(f"Original list: {arr}")
pos_arr = [i for i in arr if i > 0]
neg_arr = [i for i in arr if i < 0]
rearranged = []

i = 0
j = 0

while i < len(pos_arr) and j < len(neg_arr):
    rearranged.append(pos_arr[i])
    rearranged.append(neg_arr[j])
    i += 1
    j += 1
while i < len(pos_arr):
    rearranged.append(pos_arr[i])
    i += 1
while j < len(neg_arr):
    rearranged.append(neg_arr[j])
    j += 1 

rearranged.extend(item for item in arr if item == 0)
arr = rearranged
print(f"Rearranged list: {arr}")
    