#Time Complexity: O(m*n) in worst case
#Space Complexity: O(1)
def spiralOrder_optimal(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # traverse top row, left to right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # traverse right column, top to bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # traverse bottom row, right to left (only if a row remains)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # traverse left column, bottom to top (only if a column remains)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

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
print(spiralOrder_optimal(matrix))