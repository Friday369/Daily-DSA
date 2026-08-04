# OPTIMAL — Expand Around Center
# Time: O(n²)  Space: O(1)
def longestPalindrome_optimal():
    s = "babad"
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]     # valid palindrome before last expansion
    result = ""
    for i in range(len(s)):
        odd  = expand(i, i)          # odd length: "aba"
        even = expand(i, i + 1)      # even length: "abba"

        if len(odd)  > len(result): result = odd
        if len(even) > len(result): result = even
    print(f"Optimal Result: {result}")
longestPalindrome_optimal()