import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Step size
    
    prev = 0
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Target not in array
    
    # Linear search within the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i  # Target found at index i
    
    return -1  # Target not in array

# Example usage
sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

result = jump_search(sorted_array, target_value)
if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the array")
