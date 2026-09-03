# BRUTE FORCE — Recursion
# Time: O(2^n)  Space: O(n)
def maxSum_brute():
    arr = [6, 5, 5, 7, 4]

    def solve(n):
        if n <= 0: return 0
        if n == 1: return arr[0]
        pick    = arr[n-1] + solve(n-2)
        notpick = solve(n-1)
        return max(pick, notpick)

    print(f"Brute Force Result: {solve(len(arr))}")

maxSum_brute()
