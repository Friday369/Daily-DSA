# OPTIMAL — Modified Binary Search
# Time: O(log n) Space: O(1)

class Solution(object):
    def search(self, nums, target):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                print(f"Found {target} at index {mid}")
                return mid

            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:  
                    right = mid - 1
                else:                                  
                    left = mid + 1

            # RIGHT HALF IS SORTED
            else:
                if nums[mid] < target <= nums[right]:  
                    left = mid + 1
                else:                                   
                    right = mid - 1

        print(f"{target} not found, returning -1")
        return -1

Solution().search(None, None)