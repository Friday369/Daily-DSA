# BRUTE FORCE
# Time: O(n × m)  Space: O(n × m)
# Check every O, do BFS/DFS to see if it reaches boundary 
def replaceOX_brute():
    grid = [
        ['X', 'O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X', 'O', 'X'],
        ['X', 'X', 'X', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'O', 'X', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O']
    ]
    rows, cols = len(grid), len(grid[0])
    def touchesBoundary(r, c, visited):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return True                      # out of bounds = boundary
        if visited[r][c] or grid[r][c] == 'X':
            return False
        visited[r][c] = True
        return (touchesBoundary(r+1,c,visited) or
                touchesBoundary(r-1,c,visited) or
                touchesBoundary(r,c+1,visited) or
                touchesBoundary(r,c-1,visited))

    result = [row[:] for row in grid]       # copy grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'O':
                visited = [[False]*cols for _ in range(rows)]
                if not touchesBoundary(r, c, visited):
                    result[r][c] = 'X'      # surrounded — replace
    for row in result:
        print(row)
    print(f"Brute Force Done")
replaceOX_brute()


