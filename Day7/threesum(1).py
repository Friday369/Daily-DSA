#Time: O(n³), Space: O(n)
def threeSum_brute(nums):
    n = len(nums)
    result = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(t) for t in result]
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum_brute(nums))