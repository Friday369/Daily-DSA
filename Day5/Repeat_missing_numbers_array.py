# OPTIMAL — Math (Sum & Sum of Squares)
# Time: O(n)  Space: O(1)

def findRepeatingMissing():
    nums = [3, 1, 2, 5, 3]
    n = len(nums)

    # expected sums using formula
    expected_sum = n * (n + 1) // 2
    expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
    actual_sum = sum(nums)
    actual_sq_sum = sum(x * x for x in nums)

    diff = actual_sum - expected_sum                        # A - B
    sq_diff = actual_sq_sum - expected_sq_sum               # A² - B²
    total = sq_diff // diff                                 # A + B

    repeat = (diff + total) // 2                            # A
    missing = total - repeat                                # B

    print(f"Optimal Result: [{repeat}, {missing}]")

findRepeatingMissing()