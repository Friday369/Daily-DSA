# OPTIMAL — HashMap
# Time: O(n)  Space: O(1) — at most 26 keys
def printDuplicates_optimal():
    s = "geeksforgeeks"
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for char, count in freq.items():
        if count > 1:
            print(f"['{char}', {count}]", end=", ")
    print()
printDuplicates_optimal()