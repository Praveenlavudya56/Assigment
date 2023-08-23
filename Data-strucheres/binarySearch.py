def binarySearch(arr,l,t):
    startIndex = 0
    endIndex = l-1

    while endIndex >= startIndex:
        mid = (startIndex+endIndex)//2

        if arr[mid] == t:
            return mid
        
        elif arr[mid] >  t:
            endIndex = mid-1

        elif arr[mid] < t:
            startIndex = mid+1

    else:
        return("not found")



arr = [1,3,2,4,7,6,5,9,8,20,10]
sortedArr = sorted(arr)
print(sortedArr)
l = len(arr)
t = 10
print(binarySearch(sortedArr,l,t))

#----------------------------------------------------------------------
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid  # Found the target at index mid
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half
    
    return -1  # Target not found in the array

# Example usage
sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

result = binary_search(sorted_array, target_value)
if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the array")
