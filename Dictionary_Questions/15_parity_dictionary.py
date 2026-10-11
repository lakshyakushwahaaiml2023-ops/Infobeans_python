nums = [1,2,3,4,5,6,7,7,8,9,10]
res = {"Even" : [], "Odd" : []}

for i in nums:
    if i%2 == 0:
        res["Even"].append(i)
    else:
        res["Odd"].append(i)

print(res)