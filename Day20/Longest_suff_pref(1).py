#Time Complexity: O(n^2) Space Complexity: O(1)
def lps_brute(s):
    n = len(s)
    for length in range(n - 1, 0, -1):
        prefix = s[:length]
        suffix = s[n - length:]
        if prefix == suffix:
            return length
    return 0
s = "aabcdaabc"
print(lps_brute(s))