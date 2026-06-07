#Brute force
# Time: O(n²) Space: O(1)

class Solution(object):
    def containsDuplicate(self, nums):
        nums = [1, 2, 3, 1]  

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    print(f"Duplicate found: {nums[i]} → True")
                    return True

        print("No duplicates → False")
        return False

Solution().containsDuplicate(None)