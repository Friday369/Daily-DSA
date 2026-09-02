# OPTIMAL — HashSet
# Time: O(n)  Space: O(n)
def findPair_optimal():
    arr = [5, 20, 3, 2, 50, 80]
    x = 78
    seen = set()

    for num in arr:
        if (num + x) in seen or (num - x) in seen:
            print(f"Optimal Result: True")
            return
        seen.add(num)
    print("Optimal Result: False")
findPair_optimal()