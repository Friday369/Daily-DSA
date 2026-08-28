# BETTER — HashMap
# Time: O(n × m)  Space: O(n × m)
def findCommon_hashmap():
    mat = [
        [1, 2, 3, 4, 5],
        [2, 4, 5, 8, 10],
        [3, 5, 7, 9, 11],
        [1, 3, 5, 7, 9]
    ]
    n = len(mat)
    cnt = {}

    for i in range(n):
        cnt[mat[i][0]] = cnt.get(mat[i][0], 0) + 1
        for j in range(1, len(mat[i])):
            if mat[i][j] != mat[i][j - 1]:       # skip duplicates in row
                cnt[mat[i][j]] = cnt.get(mat[i][j], 0) + 1

    for ele, c in cnt.items():
        if c == n:
            print(f"HashMap Result: {ele}")
            return

    print("HashMap Result: -1")
findCommon_hashmap()

