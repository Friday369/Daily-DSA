# OPTIMAL — DFS + Early Termination with frequency check
# Time: O(m × n × 4^L)  Space: O(L)
def exist_optimal():
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCCED"
    rows, cols = len(board), len(board[0])
    # early exit: check if board has enough chars for word
    from collections import Counter
    board_count = Counter(c for row in board for c in row)
    word_count = Counter(word)
    for ch, cnt in word_count.items():
        if board_count[ch] < cnt:
            print("Optimal Result: False")
            return
    # if last char is rarer, search word in reverse (prune faster)
    if board_count[word[0]] > board_count[word[-1]]:
        word = word[::-1]
    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False
        temp = board[r][c]
        board[r][c] = "#"
        found = (dfs(r+1, c, idx+1) or
                 dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or
                 dfs(r, c-1, idx+1))
        board[r][c] = temp
        return found
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                print("Optimal Result: True")
                return
    print("Optimal Result: False")
exist_optimal()