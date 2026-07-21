# OPTIMAL — Two Pointer Greedy
# Time: O(n)  Space: O(1)

def minMerges_optimal():
    arr = [1, 4, 5, 1]

    left, right = 0, len(arr) - 1
    ops = 0

    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        elif arr[left] < arr[right]:
            arr[left + 1] += arr[left]   # merge left into next
            left += 1
            ops += 1
        else:
            arr[right - 1] += arr[right]  # merge right into prev
            right -= 1
            ops += 1

    print(f"Optimal Result: {ops}")

minMerges_optimal()