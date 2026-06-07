#Optimal Solution 
# Time: O(n) | Space: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        nums = [1, 2, 3, 1]  # Expected: True

        seen = set()
        for num in nums:
            if num in seen:
                print(f"Duplicate found: {num} → True")
                return True
            seen.add(num)

        print("No duplicates → False")
        return False

Solution().containsDuplicate(None)