# BETTER — Sort + Two Pointer
# Time: O(n log n)  Space: O(1)
def findPair_twopointer():
    arr = [5, 20, 3, 2, 50, 80]
    x = 78
    arr.sort()
    i, j = 0, 1
    while i < len(arr) and j < len(arr):
        diff = arr[j] - arr[i]
        if diff == x and i != j:
            print(f"Two Pointer Result: True → pair ({arr[i]}, {arr[j]})")
            return
        elif diff < x:
            j += 1
        else:
            i += 1
            if i == j:
                j += 1
    print("Two Pointer Result: False")
findPair_twopointer()

