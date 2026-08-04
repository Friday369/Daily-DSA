# BRUTE FORCE
# Time: O(n³)  Space: O(1)

def longestPalindrome_brute():
    s = "babad"
    def isPalindrome(sub):
        return sub == sub[::-1]
    result = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if isPalindrome(s[i:j]) and len(s[i:j]) > len(result):
                result = s[i:j]
    print(f"Brute Force Result: {result}")
longestPalindrome_brute()


