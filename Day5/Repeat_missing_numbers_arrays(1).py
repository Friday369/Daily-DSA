# BRUTE FORCE
# Time: O(n²)  Space: O(1)

def findRepeatingMissing():
    nums = [3, 1, 2, 5, 3]
    n = len(nums)
    repeat = -1
    missing = -1

    for i in range(1, n + 1):
        count = 0
        for j in range(n):
            if nums[j] == i:
                count += 1

        if count == 2:
            repeat = i
        if count == 0:
            missing = i

    print(f"Brute Force Result: [{repeat}, {missing}]")
findRepeatingMissing()
