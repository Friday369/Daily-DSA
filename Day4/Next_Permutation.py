# OPTIMAL
# Time: O(n)  Space: O(1)

def nextPermutation():
    nums = [1, 2, 3]
    n = len(nums)
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot =i
            break
    if pivot == -1:
        nums.reverse()
        print(f"Optimal Result: {nums}")
        return
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            nums[pivot], nums[i] = nums[i], nums[pivot]
            break

    nums[pivot + 1:] = reversed(nums[pivot + 1:])
    print(f"Optimal Result: {nums}")
nextPermutation()