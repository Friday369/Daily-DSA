# OPTIMAL — Binary Search
# Time: O(log n)  Space: O(1)

def findMin():
    nums = [3, 4, 5, 1, 2]

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1      
        else:
            right = mid         

    print(f"Optimal Result: {nums[left]}")

findMin()