arr = [1, 2, 3, 7, 5,12,23,111]
left = 0
right = 0
current_sum = 0
target = 13

while left < len(arr) and right < len(arr):
    current_sum += arr[right]

    while current_sum > target:
        current_sum -= arr[left]
        left+=1
    else:
        right+=1
        if current_sum == target:
                print(f"Subarray found from index {left} to {right-1}")
                break
    
