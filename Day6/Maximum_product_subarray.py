# OPTIMAL — Track Max and Min
# Time: O(n)  Space: O(1)

def maxProduct_optimal():
    nums = [2, 3, -2, 4]

    max_prod = nums[0]
    curr_max = nums[0]
    curr_min = nums[0]

    for i in range(1, len(nums)):
        # when multiplied by negative, max becomes min and min becomes max
        if nums[i] < 0:
            curr_max, curr_min = curr_min, curr_max

        curr_max = max(nums[i], curr_max * nums[i])
        curr_min = min(nums[i], curr_min * nums[i])

        max_prod = max(max_prod, curr_max)

    print(f"Optimal Result: {max_prod}")

maxProduct_optimal()
