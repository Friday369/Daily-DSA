# BRUTE FORCE — Sorting
# Time: O(n log n)  Space: O(1)
# Sort string, then count consecutive same characters
def printDuplicates_brute():
    s = "geeksforgeeks"
    s = ''.join(sorted(s))     # group same chars together
    i = 0
    while i < len(s):
        count = 1
        while i + count < len(s) and s[i] == s[i + count]:
            count += 1
        if count > 1:
            print(f"['{s[i]}', {count}]", end=", ")
        i += count
    print()
printDuplicates_brute()


