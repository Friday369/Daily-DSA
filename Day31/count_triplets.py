# OPTIMAL — Sort + Two Pointer
# Time: O(n²)  Space: O(1)
def countTriplets_optimal():
    arr = [-2, 0, 1, 3]
    sum_val = 2
    arr.sort()
    n = len(arr)
    count = 0
    for i in range(n - 2):
        j, k = i + 1, n - 1
        while j < k:
            if arr[i] + arr[j] + arr[k] < sum_val:
                count += (k - j)      # all elements between j and k work!
                j += 1
            else:
                k -= 1
    print(f"Optimal Result: {count}")
countTriplets_optimal()