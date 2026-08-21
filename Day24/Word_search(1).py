# BRUTE FORCE
# Time: O(m × n × 4^L)  Space: O(L)
def exist_brute():
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCCED"
    rows, cols = len(board), len(board[0])
    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False
        temp = board[r][c]
        board[r][c] = "#"           # mark visited
        found = (dfs(r+1, c, idx+1) or
                 dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or
                 dfs(r, c-1, idx+1))

        board[r][c] = temp          # restore
        return found
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                print(f"Brute Force Result: True")
                return
    print(f"Brute Force Result: False")

exist_brute()


