#Time Complexity: O(m*n) in worst case
#Space Complexity: O(1)
def spiralOrder_brute(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    result = []

    # direction vectors: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_index = 0

    row, col = 0, 0
    for _ in range(rows * cols):
        result.append(matrix[row][col])
        visited[row][col] = True

        next_row = row + directions[dir_index][0]
        next_col = col + directions[dir_index][1]

        # check if next cell is valid and unvisited, else turn
        if (0 <= next_row < rows and 0 <= next_col < cols and not visited[next_row][next_col]):
            row, col = next_row, next_col
        else:
            dir_index = (dir_index + 1) % 4
            row += directions[dir_index][0]
            col += directions[dir_index][1]

    return result
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Input Matrix:")
for row in matrix:    
    print(row)  
print("Spiral Order:")
print(spiralOrder_brute(matrix))