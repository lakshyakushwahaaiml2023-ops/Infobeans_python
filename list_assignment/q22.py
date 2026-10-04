arr = [1,2,3,4,5]
target = 3
near_low = float('-inf')
near_high = float('inf')
for i in arr:
    if i < target and i > near_low:
        near_low = i
    elif i > target and i < near_high:
        near_high = i
print(f"Nearest lower: {near_low}")
print(f"Nearest greater: {near_high}")