# BRUTE FORCE
# Time: O(n²)  Space: O(n)
def removeConsecutiveDuplicates_brute():
    s = "aabbccaab"
    result = list(s)
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(result) - 1:
            if result[i] == result[i + 1]:
                result.pop(i)
                changed = True
            else:
                i += 1
    print(f"Brute Force Result: {''.join(result)}")
removeConsecutiveDuplicates_brute()