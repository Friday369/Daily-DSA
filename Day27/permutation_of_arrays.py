# OPTIMAL — Sort a ascending, sort b descending
# Time: O(n log n)  Space: O(1)
def isPossible_optimal():
    a = [2, 1, 3]
    b = [7, 8, 9]
    k = 10
    a.sort()                    # ascending
    b.sort(reverse=True)        # descending

    for i in range(len(a)):
        if a[i] + b[i] < k:
            print(f"Optimal Result: False")
            return
    print(f"Optimal Result: True")
isPossible_optimal()