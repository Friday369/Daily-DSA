# BRUTE FORCE
# Time: O(n³)  Space: O(n)
def lengthOfLongestSubstring_brute():
    s = "abcabcbb"
    max_len = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(set(s[i:j])) == j - i:    # all unique
                max_len = max(max_len, j - i)
    print(f"Brute Force Result: {max_len}")
lengthOfLongestSubstring_brute()


