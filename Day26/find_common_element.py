# OPTIMAL — Multi-Pointer (rows are sorted!)
# Time: O(n × m)  Space: O(n)
def findCommon_optimal():
    mat = [
        [1, 2, 3, 4, 5],
        [2, 4, 5, 8, 10],
        [3, 5, 7, 9, 11],
        [1, 3, 5, 7, 9]
    ]
    n = len(mat)
    m = len(mat[0])
    ptr = [0] * n                  # one pointer per row
    while True:
        mx = max(mat[i][ptr[i]] for i in range(n))

        if all(mat[i][ptr[i]] == mx for i in range(n)):
            print(f"Optimal Result: {mx}")
            return

        for i in range(n):
            if mat[i][ptr[i]] < mx:
                ptr[i] += 1
                if ptr[i] == m:
                    print("Optimal Result: -1")
                    return

findCommon_optimal()