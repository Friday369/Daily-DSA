# OPTIMAL — Space Optimized DP
# Time: O(n)  Space: O(1)
def maxSum_optimal():
    arr = [6, 5, 5, 7, 4]
    n = len(arr)
    if n == 1:
        print(f"Optimal Result: {arr[0]}")
        return
    second_last = 0
    last = arr[0]
    for i in range(1, n):
        curr = max(arr[i] + second_last, last)
        second_last = last
        last = curr
    print(f"Optimal Result: {last}")
maxSum_optimal()