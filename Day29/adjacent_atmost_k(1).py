# BRUTE FORCE — Linear Search
# Time: O(n)  Space: O(1)
# Check every element one by one
def searchKStep_brute():
    arr = [4, 5, 6, 7, 6]
    k = 1
    x = 6

    for i in range(len(arr)):
        if arr[i] == x:
            print(f"Brute Force Result: {i}")
            return

    print("Brute Force Result: -1")
searchKStep_brute()
