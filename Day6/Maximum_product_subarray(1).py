# BRUTE FORCE
# Time: O(n²)  Space: O(1)

def maxProduct():
    nums = [2, 3, -2, 4]

    max_prod = float('-inf')

    for i in range(len(nums)):
        current_prod = 1
        for j in range(i, len(nums)):
            current_prod *= nums[j]
            max_prod = max(max_prod, current_prod)

    print(f"Brute Force Result: {max_prod}")

maxProduct()