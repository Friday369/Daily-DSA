# OPTIMAL — Expand Around Center
# Time: O(n²)  Space: O(1)
def countSubstrings_optimal():
    s = "abc"
    count = 0
    def expand(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    for i in range(len(s)):
        expand(i, i)        # odd length palindromes
        expand(i, i + 1)    # even length palindromes
    print(f"Optimal Result: {count}")
countSubstrings_optimal()