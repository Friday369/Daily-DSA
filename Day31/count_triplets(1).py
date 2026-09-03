# BRUTE FORCE
# Time: O(n³)  Space: O(1)
def countTriplets_brute():
    arr = [-2, 0, 1, 3]
    sum_val = 2
    n = len(arr)
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] < sum_val:
                    count += 1
    print(f"Brute Force Result: {count}")
countTriplets_brute()
