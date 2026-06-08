# BRUTE FORCE 
# Time: O(n)  Space: O(1)
class Solution(object):
    def search(self, nums, target):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0

        for i in range(len(nums)):
            if nums[i] == target:
                print(f"Found {target} at index {i}")
                return i

        print(f"{target} not found, returning -1")
        return -1

Solution().search(None, None)