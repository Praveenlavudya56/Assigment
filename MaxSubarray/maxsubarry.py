
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6 in python


# def maxSubArray(nums):
#     maxSum = -99999999999999999999999999999999999999999999999999
#     start =0
#     end = 0

#     for i in range(len(nums)):
#         currentSum = 0
#         for j in range(i, len(nums)):
#             currentSum = currentSum + nums[j]
#             if currentSum>maxSum:
#                 maxSum = currentSum
#                 start = i
#                 end  = j
#     return(maxSum,nums[start:end+1])

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(nums))

#-------------------------------------------------------------------------------------

# def max_subarray_sum(nums):
#     if not nums:
#         return 0
    
#     max_sum = current_sum = nums[0]
    
#     for num in nums[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
    
#     return max_sum

# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# result = max_subarray_sum(nums)
# print(result)  # Output will be 6
#-------------------------------------------------------------------------------------
#Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.


# def max_subarray_sum(nums):
#     if not nums:
#         return 0
    
#     max_sum = current_sum = nums[0]
    
#     for num in nums[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
    
#     return max_sum

# nums = [1]
# result = max_subarray_sum(nums)
# print(result)  # Output will be 1

