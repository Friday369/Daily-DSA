# BRUTE FORCE — Linear Search
# Time: O(n)  Space: O(1)
def ceilSearch_brute():
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 5
    if x <= arr[0]:
        print(f"Brute Force Result: index=0, value={arr[0]}")
        return
    for i in range(len(arr) - 1):
        if arr[i] == x:
            print(f"Brute Force Result: index={i}, value={arr[i]}")
            return
        if arr[i] < x and arr[i + 1] >= x:
            print(f"Brute Force Result: index={i+1}, value={arr[i+1]}")
            return
    print("Brute Force Result: -1 (no ceiling exists)")
ceilSearch_brute()


