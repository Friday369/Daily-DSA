# OPTIMAL — Step Jump Search
# Time: O(n/k)  Space: O(1)
# Use k-step property to skip positions
def searchKStep_optimal():
    arr = [4, 5, 6, 7, 6]
    k = 1
    x = 6
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == x:
            print(f"Optimal Result: {i}")
            return
        # jump by diff/k positions since value can change by at most k per step
        jump = max(1, abs(arr[i] - x) // k)
        i += jump
    print("Optimal Result: -1")
searchKStep_optimal()