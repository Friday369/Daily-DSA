#Time complexity: O(n)  Space complexity: O(1)
def characterReplacement_optimal(s, k):
    freq = {}
    left = 0
    max_freq = 0
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])

        window_len = right - left + 1

        # if changes needed exceed k, shrink window from the left
        if window_len - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

s = "AABABBA"
k = 1
print(characterReplacement_optimal(s, k))