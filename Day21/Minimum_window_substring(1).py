from collections import Counter
def minWindow_brute(s, t):
    n = len(s)
    need = Counter(t)
    min_len = float('inf')
    result = ""
    for i in range(n):
        for j in range(i, n):
            window = s[i:j+1]
            window_count = Counter(window)
            valid = True
            for ch in need:
                if window_count[ch] < need[ch]:
                    valid = False
                    break
            if valid and (j - i + 1) < min_len:
                min_len = j - i + 1
                result = window
    return result
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow_brute(s, t))