# BRUTE FORCE
# Time: O(n²)  Space: O(n²)
def rotate_brute():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]
    for row in result:
        print(row)
    print(f"Brute Force Result: {result}")
rotate_brute()

