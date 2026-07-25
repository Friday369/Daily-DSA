# OPTIMAL — Mo's Algorithm (Square Root Decomposition)
# Time: O((n + m) × √n)  Space: O(m)
import math
def mosAlgorithm_optimal():
    arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    queries = [[0, 4], [1, 3], [2, 4]]
    n = len(arr)
    block = int(math.sqrt(n))
    sorted_queries = sorted(
        enumerate(queries),
        key=lambda x: (x[1][0] // block, x[1][1])
    )
    curr_sum = 0
    curr_L = 0
    curr_R = -1
    results = [0] * len(queries)
    for orig_idx, q in sorted_queries:
        L, R = q
        while curr_R < R:
            curr_R += 1
            curr_sum += arr[curr_R]

        while curr_L > L:
            curr_L -= 1
            curr_sum += arr[curr_L]

        while curr_R > R:
            curr_sum -= arr[curr_R]
            curr_R -= 1
        while curr_L < L:
            curr_sum -= arr[curr_L]
            curr_L += 1
        results[orig_idx] = curr_sum
    
    for i, q in enumerate(queries):
        print(f"Sum of {q} is {results[i]}")
mosAlgorithm_optimal()