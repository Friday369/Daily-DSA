# BRUTE FORCE
# Time: O(n × m × n)  Space: O(1)
# For each element in first row, check if it exists in all other rows
def findCommon_brute():
    mat = [
        [1, 2, 3, 4, 5],
        [2, 4, 5, 8, 10],
        [3, 5, 7, 9, 11],
        [1, 3, 5, 7, 9]
    ]
    n = len(mat)
    m = len(mat[0])
    for i in range(m):
        check = mat[0][i]
        count = 1

        for j in range(1, n):
            for k in range(m):
                if mat[j][k] == check:
                    count += 1
                    break
        if count == n:
            print(f"Brute Force Result: {check}")
            return

    print("Brute Force Result: -1")

findCommon_brute()


