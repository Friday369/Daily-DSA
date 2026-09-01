# OPTIMAL — Binary Search
# Time: O(log n)  Space: O(1)
def ceilSearch_optimal():
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 5
    lo, hi = 0, len(arr) - 1
    res = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] < x:
            lo = mid + 1
        else:                    # potential ceiling found
            res = mid
            hi = mid - 1        # try finding smaller ceiling on left
    if res == -1:
        print("Optimal Result: -1 (no ceiling exists)")
    else:
        print(f"Optimal Result: index={res}, value={arr[res]}")
ceilSearch_optimal()