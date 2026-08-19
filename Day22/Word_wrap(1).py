#Time Complexity: O(n^2) in worst case
#Space Complexity: O(n)
def solveWordWrap_brute(nums, k):
    n = len(nums)

    def cost(i, j):
        # cost of putting words[i..j] on a single line
        line_len = j - i  # spaces between words
        for idx in range(i, j + 1):
            line_len += nums[idx]
        if line_len > k:
            return float('inf')
        if j == n - 1:
            return 0  # last line has no penalty
        return (k - line_len) ** 3

    def solve(i):
        if i == n:
            return 0
        best = float('inf')
        for j in range(i, n):
            line_cost = cost(i, j)
            if line_cost == float('inf'):
                break
            best = min(best, line_cost + solve(j + 1))
        return best

    return solve(0)

nums = [3, 2, 2, 5]
k = 6
print("Input:", nums)
print("Minimum cost:", solveWordWrap_brute(nums, k))