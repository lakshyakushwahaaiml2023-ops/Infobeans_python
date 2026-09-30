l = [1,2,3,4,5,6,7,8,1,2,1,1]

'''
l = [1,2,3,4,5]
sum = 0
for i in l:
    sum = sum+i
print(sum)'''


'''sum_even = 0
sum_odd = 0

for i in range(len(l)):
    if i%2 == 0:
        sum_even += l[i]
    else:
        sum_odd += l[i]

print(sum_even)
print(sum_odd)'''


'''target = int(input("Enter a number: "))
for i in range(len(l)):
    if l[i] == target:
        print(f"Target found at {i} index")
        break
else:
        print("Target not found")'''


'''target = 10
result = []
for i in range(len(l)):
    if l[i] == target:
        result.append(i)
if result:
    print(f"Target found at {result}")
else:
    print("Element not found")'''



'''l1 = [1,2,2,3,4,5,1,1,2,34,4]
target = int(input("Enter a number: "))
seen = {}
for index, value in enumerate(l1):
    dif = target - value

    if dif in seen:
        print(seen[dif], index)
        break
    else:
        seen[value] = index
else:
    print("Target sum pair not found")'''



'''arr1 = [1,2,2,3,4,5]
arr2 = [2,3,3,4,4,4,5,6,7]
res = []

i = 0
j = 0

while i<len(arr1) and j<len(arr2):
    if arr1[i] < arr2[j]:
        res.append(arr1[i])
        i+=1
    else:
        res.append(arr2[j])
        j+=1

while i<len(arr1):
    res.append(arr1[i])
    i+=1

while j<len(arr2):
    res.append(arr2[j])
    j+=1

print(f"Array 1 : {arr1}")
print(f"Array 2 : {arr2}")
print(f"Merge array : {res}")'''