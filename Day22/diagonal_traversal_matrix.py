#Time Complexity: O(n*m) in worst case
#Space Complexity: O(n*m)
def diagonalTraversal_optimal(matrix):
    if not matrix or not matrix[0]:
        return []
    n, m = len(matrix), len(matrix[0])
    result = []
    for d in range(n + m - 1):
        # determine starting row/col for this diagonal
        if d < m:
            row, col = 0, d
        else:
            row, col = d - m + 1, m - 1

        current_diagonal = []
        while row < n and col >= 0:
            current_diagonal.append(matrix[row][col])
            row += 1
            col -= 1

        if d % 2 == 0:
            result.extend(reversed(current_diagonal))
        else:
            result.extend(current_diagonal)
    return result
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Input Matrix:")
for row in matrix:  
    print(row)  
print("Diagonal Traversal:")    
print(diagonalTraversal_optimal(matrix))