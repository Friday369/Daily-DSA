#Time Complexity: O(m*n) in worst case
#Space Complexity: O(1)
def setZeroes_optimal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
    # use first row/column as marker space for the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    # zero out cells based on markers (skip first row/col for now)
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # handle first row and first column separately, using the flags
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0

    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
print("Input Matrix:")
for row in matrix:
    print(row)
print("Output Matrix:")
for row in setZeroes_optimal(matrix):
    print(row)