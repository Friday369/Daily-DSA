# BRUTE FORCE
# Time: O(n²) Space: O(1)

def chocolatedistribution():
    arr = [3, 4, 1, 9, 56, 7, 9, 12]
    m = 5

    arr.sort()
    min_diff = float('inf')

    for i in range(len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)

    print(f"Minimum difference: {min_diff}")  # Output: 6

chocolatedistribution()