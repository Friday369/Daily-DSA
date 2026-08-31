# BRUTE FORCE
# Time: O(n³ × m³)  Space: O(1)
# Check every possible rectangle in the matrix
def maxRectangle_brute():
    mat = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]
    ]
    n, m = len(mat), len(mat[0])
    max_area = 0
    for r1 in range(n):
        for c1 in range(m):
            for r2 in range(r1, n):
                for c2 in range(c1, m):
                    # check if all cells in rectangle are 1
                    all_ones = True
                    for r in range(r1, r2 + 1):
                        for c in range(c1, c2 + 1):
                            if mat[r][c] == 0:
                                all_ones = False
                                break
                        if not all_ones:
                            break
                    if all_ones:
                        area = (r2 - r1 + 1) * (c2 - c1 + 1)
                        max_area = max(max_area, area)
    print(f"Brute Force Result: {max_area}")
maxRectangle_brute()


