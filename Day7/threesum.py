#Time: O(n²), Space: O(1) 
def threeSum_optimal(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        # skip duplicate values for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # since sorted, if smallest possible sum > 0, no triplet works
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # skip duplicates for left and right
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum_optimal(nums))  # [[-1, -1, 2], [-1, 0, 1]]