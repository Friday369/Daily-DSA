# BRUTE FORCE
# Time: O(n²)  Space: O(1)
# Try every subarray, check if sum % k == 0

def longestSubarrayDivK_brute():
    arr = [2, 7, 6, 1, 4, 5]
    k = 3

    max_len = 0

    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum = (curr_sum + arr[j]) % k
            if curr_sum == 0:
                max_len = max(max_len, j - i + 1)

    print(f"Brute Force Result: {max_len}")

longestSubarrayDivK_brute()