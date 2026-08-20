#Time Complexity: O(m*n) in worst case  
#Space Complexity: O(1)
def setZeroes_brute(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    zero_positions = []
    # first pass: find all zero positions
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_positions.append((i, j))
    # second pass: mark entire row and column for each zero found
    for (r, c) in zero_positions:
        for j in range(cols):
            matrix[r][j] = 0
        for i in range(rows):
            matrix[i][c] = 0
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
for row in setZeroes_brute(matrix):
    print(row)