#Time Complexity: O(n)  Space Complexity: O(n)

from collections import Counter
def smallestWindow_optimal(s, t):
    if not t or not s:
        return ""
    need = Counter(t)
    required = len(need)          
    window_counts = {}
    formed = 0                     
    left = 0
    min_len = float('inf')
    min_start = 0
    for right in range(len(s)):
        ch = s[right]
        window_counts[ch] = window_counts.get(ch, 0) + 1
        if ch in need and window_counts[ch] == need[ch]:
            formed += 1
        while left <= right and formed == required:
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                min_start = left
            left_ch = s[left]
            window_counts[left_ch] -= 1
            if left_ch in need and window_counts[left_ch] < need[left_ch]:
                formed -= 1

            left += 1
    return "" if min_len == float('inf') else s[min_start:min_start + min_len]
s = "timetopractice"
t = "toc"
print(smallestWindow_optimal(s, t))