#Time Complexity: O(n*m) in worst case
#Space Complexity: O(n*m)
def diagonalTraversal_brute(matrix):
    if not matrix or not matrix[0]:
        return []
    n, m = len(matrix), len(matrix[0])
    diagonals = {}
    # group elements by i+j (each diagonal shares the same i+j value)
    for i in range(n):
        for j in range(m):
            key = i + j
            if key not in diagonals:
                diagonals[key] = []
            diagonals[key].append(matrix[i][j])

    result = []
    for key in range(n + m - 1):
        line = diagonals[key]
        if key % 2 == 0:
            result.extend(reversed(line))  # even diagonals go bottom-to-top
        else:
            result.extend(line)             # odd diagonals go top-to-bottom

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
print(diagonalTraversal_brute(matrix))