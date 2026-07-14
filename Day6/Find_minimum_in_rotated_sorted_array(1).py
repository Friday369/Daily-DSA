# BRUTE FORCE
# Time: O(n)  Space: O(1)

def findMin():
    nums = [3, 4, 5, 1, 2]

    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num

    print(f"Brute Force Result: {min_val}")

findMin()