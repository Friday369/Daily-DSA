# BETTER — DP with array (Tabulation)
# Time: O(n)  Space: O(n)
def maxSum_dp():
    arr = [6, 5, 5, 7, 4]
    n = len(arr)

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = arr[0]
    for i in range(2, n + 1):
        dp[i] = max(arr[i-1] + dp[i-2], dp[i-1])

    print(f"DP Result: {dp[n]}")

maxSum_dp()
