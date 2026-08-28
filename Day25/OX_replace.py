# OPTIMAL — Flood Fill from Boundary
# Time: O(n × m)  Space: O(n × m)
def replaceOX_optimal():
    grid = [
        ['X', 'O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X', 'O', 'X'],
        ['X', 'X', 'X', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'O', 'X', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O']
    ]
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != 'O':
            return
        grid[r][c] = '#'                    # mark safe O
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    # STEP 1: mark all O's connected to boundary as '#'
    for r in range(rows):
        if grid[r][0] == 'O':    dfs(r, 0)
        if grid[r][cols-1] == 'O': dfs(r, cols-1)
    for c in range(cols):
        if grid[0][c] == 'O':    dfs(0, c)
        if grid[rows-1][c] == 'O': dfs(rows-1, c)

    # STEP 2: remaining O's are surrounded → replace with X
    # STEP 3: restore '#' back to O
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'O':
                grid[r][c] = 'X'
            elif grid[r][c] == '#':
                grid[r][c] = 'O'

    for row in grid:
        print(row)
    print("Optimal Done")
replaceOX_optimal()