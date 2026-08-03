#Time complexity: O(n^2)  Space complexity: O(n)
def characterReplacement_brute(s, k):
    n = len(s)
    max_len = 0

    for i in range(n):
        freq = {}
        max_freq = 0
        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_freq = max(max_freq, freq[s[j]])

            window_len = j - i + 1
            changes_needed = window_len - max_freq

            if changes_needed <= k:
                max_len = max(max_len, window_len)

    return max_len

s = "AABABBA"
k = 1
print(characterReplacement_brute(s, k))