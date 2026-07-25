# BRUTE FORCE
# Time: O(n × m)  Space: O(1)
def mosAlgorithm_brute():
    arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    queries = [[0, 4], [1, 3], [2, 4]]

    for q in queries:
        L, R = q
        total = 0
        for i in range(L, R + 1):
            total += arr[i]
        print(f"Sum of {q} is {total}")

mosAlgorithm_brute()


