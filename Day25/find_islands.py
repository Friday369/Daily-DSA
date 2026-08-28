# OPTIMAL — DFS with in-place marking (no extra visited matrix)
# Time: O(n × m)  Space: O(n × m) recursion stack only
def numIslands_optimal():
    grid = [
        ['L', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'L'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'W', 'W', 'W', 'W'],
        ['L', 'W', 'L', 'L', 'W']
    ]
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != 'L':
            return
        grid[r][c] = '#'              # mark visited in-place
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'L':
                dfs(r, c)
                islands += 1
    print(f"Optimal Result: {islands}")
numIslands_optimal()