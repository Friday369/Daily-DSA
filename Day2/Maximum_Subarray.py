#KADANE'S ALGORITHM
#Time: O(n)  Space: O(1)

def maxSubArray():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    print(f"Kadane's Result: {max_sum}")  

maxSubArray()