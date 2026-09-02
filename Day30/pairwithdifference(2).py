# BRUTE FORCE — Nested Loops
# Time: O(n²)  Space: O(1)
def findPair_brute():
    arr = [5, 20, 3, 2, 50, 80]
    x = 78

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == x:
                print(f"Brute Force Result: True → pair ({arr[i]}, {arr[j]})")
                return

    print("Brute Force Result: False")
findPair_brute()


