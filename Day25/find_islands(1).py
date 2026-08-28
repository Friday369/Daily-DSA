# BRUTE FORCE — Check every unvisited land cell naively
# Time: O(n × m)  Space: O(n × m)
def numIslands_brute():
    grid = [
        ['L', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'L'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'W', 'W', 'W', 'W'],
        ['L', 'W', 'L', 'L', 'W']
    ]
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] or grid[r][c] == 'W':
            return
        visited[r][c] = True
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'L' and not visited[r][c]:
                dfs(r, c)
                islands += 1
    print(f"Brute Force Result: {islands}")
numIslands_brute()


