# OPTIMAL — Custom Comparator Sort
# Time: O(n log n)  Space: O(n)

from functools import cmp_to_key

def largestNumber_optimal():
    arr = [3, 30, 34, 5, 9]

    def compare(a, b):
        if a + b > b + a:
            return -1    # a should come first
        else:
            return 1     # b should come first

    nums = list(map(str, arr))
    nums.sort(key=cmp_to_key(compare))

    if nums[0] == "0":           # edge case: all zeros
        print("Optimal Result: 0")
        return

    result = "".join(nums)
    print(f"Optimal Result: {result}")

largestNumber_optimal()