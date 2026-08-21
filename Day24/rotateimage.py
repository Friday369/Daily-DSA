# OPTIMAL — Transpose + Reverse
# Time: O(n²)  Space: O(1)
def rotate_optimal():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    n = len(matrix)
    # STEP 1: Transpose (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # STEP 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
    print(f"Optimal Result: {matrix}")
rotate_optimal()