l1 = [1,2,3,4,5,6,7]
i = 0
j = len(l1) - 1

print(f"Original list: {l1}")

while i< j:
    l1[i], l1[j] = l1[j], l1[i]
    i+=1
    j-=1

print(f"Reversed list: {l1}")