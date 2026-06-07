# BRUTE FORCE 
# Time: O(n²) Space: O(1)

def maxsubarray():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = float('-inf')
    
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    
    print(f"Brute Force Result: {max_sum}") 

maxsubarray()