#Time Complexity: O(n^2) in worst case
#Space Complexity: O(n)
def solveWordWrap_optimal(nums, k):
    n = len(nums)
    dp = [float('inf')] * (n + 1)
    dp[n] = 0  # base case: no words left, no cost
    for i in range(n - 1, -1, -1):
        line_len = -1  # start at -1 so first word doesn't add an extra space
        for j in range(i, n):
            line_len += nums[j] + 1
            if line_len > k:
                break
            if j == n - 1:
                line_cost = 0  # last line has no penalty
            else:
                line_cost = (k - line_len) ** 3
            if line_cost != float('inf') and dp[j + 1] != float('inf'):
                dp[i] = min(dp[i], line_cost + dp[j + 1])
    return dp[0]
nums = [3, 2, 2, 5]
print("Input:", nums)
k = 6
print("Minimum cost:", solveWordWrap_optimal(nums, k))