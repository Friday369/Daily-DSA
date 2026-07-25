# OPTIMAL — Prefix Sum + HashMap
# Time: O(n)  Space: O(min(n, k))
def longestSubarrayDivK_optimal():
    arr = [2, 7, 6, 1, 4, 5]
    k = 3
    prefix_mod = {}
    curr_sum = 0
    max_len = 0
    for i in range(len(arr)):
        curr_sum = ((curr_sum + arr[i]) % k + k) % k
        if curr_sum == 0:
            max_len = i + 1
        elif curr_sum in prefix_mod:
            max_len = max(max_len, i - prefix_mod[curr_sum])
        else:
            prefix_mod[curr_sum] = i
    print(f"Optimal Result: {max_len}")
longestSubarrayDivK_optimal()   