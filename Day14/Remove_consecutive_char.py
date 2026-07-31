# OPTIMAL — Single Pass
# Time: O(n)  Space: O(n)
def removeConsecutiveDuplicates_optimal():
    s = "aabbccaab"
    result = []
    for c in s:
        if not result or result[-1] != c:
            result.append(c)
    print(f"Optimal Result: {''.join(result)}")
removeConsecutiveDuplicates_optimal()