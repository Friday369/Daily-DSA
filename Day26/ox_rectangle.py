# OPTIMAL — Spiral Fill
# Time: O(n × m)  Space: O(n × m)
def fillMatrix_optimal():
    m, n = 5, 5
    mat = [[''] * n for _ in range(m)]
    k, l = 0, 0
    r, c = m, n
    char = 'X'
    while k < m and l < n:

        # fill top row
        for i in range(l, n):
            mat[k][i] = char
        k += 1
        # fill right column
        for i in range(k, m):
            mat[i][n - 1] = char
        n -= 1

        # fill bottom row
        if k < m:
            for i in range(n - 1, l - 1, -1):
                mat[m - 1][i] = char
            m -= 1

        # fill left column
        if l < n:
            for i in range(m - 1, k - 1, -1):
                mat[i][l] = char
            l += 1

        # flip character
        char = '0' if char == 'X' else 'X'

    for row in mat:
        print(' '.join(row))
    print("Optimal Done")

fillMatrix_optimal()