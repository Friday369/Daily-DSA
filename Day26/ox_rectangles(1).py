# BRUTE FORCE
# Time: O(n × m)  Space: O(n × m)
# Fill layer by layer checking position of each cell
def fillMatrix_brute():
    m, n = 5, 5
    mat = [[''] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # find which layer this cell belongs to
            layer = min(i, j, m - 1 - i, n - 1 - j)
            mat[i][j] = 'X' if layer % 2 == 0 else '0'

    for row in mat:
        print(' '.join(row))
    print(f"Brute Force Done")

fillMatrix_brute()


