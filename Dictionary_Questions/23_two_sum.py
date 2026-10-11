nums = [1,2,3,4,5,6,7,8,9,10]
print(f"Array : {nums}")
target = 14
print(f"Target : {target}")
seen = {}

for i in range(len(nums)):
    rem = target - nums[i]
    if rem in seen:
        print(f"Two sum pairs : {seen[rem], i} ==> {rem} + {nums[i]} = {target}")
        break
    else:
        seen[nums[i]] = i
else:
    print("No two sum pair found")