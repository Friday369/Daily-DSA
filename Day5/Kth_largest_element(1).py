# BRUTE FORCE
# Time: O(n log n)  Space: O(1)

def findKthLargest():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    nums.sort(reverse=True)
    print(f"Brute Force Result: {nums[k-1]}")

findKthLargest()