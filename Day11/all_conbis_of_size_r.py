# OPTIMAL — Fix one element at a time (standard backtracking)
# Time: O(r * C(n, r))   Space: O(r) recursion depth
def combinations_optimal(arr, r):
    n = len(arr)
    result = []
    data = []
    def helper(start):
        if len(data) == r:
            result.append(data.copy())
            return
        for i in range(start, n):
            data.append(arr[i])
            helper(i + 1)
            data.pop()
    helper(0)
    return result
arr = [1, 2, 3, 4]
r = 2
print("Optimal:", combinations_optimal(arr, r))