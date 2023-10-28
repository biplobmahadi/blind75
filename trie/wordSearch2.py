def findWords(board, words):
    visited = [[False]*len(board[0]) for _ in range(len(board))]
    def exist2(word):
        def dfs(i, row, col):
            if i == len(word):
                return True
            if (row<0 or col<0 or row>=len(board) or 
                col>=len(board[0]) or visited[row][col] or 
                board[row][col] != word[i]):
                return False
            visited[row][col] = True
            res = (dfs(i+1, row-1, col) or
                dfs(i+1, row, col+1) or
                dfs(i+1, row+1, col) or
                dfs(i+1, row, col-1))
            visited[row][col] = False
            return res
        for p in range(len(board)):
            for q in range(len(board[0])):
                if dfs(0, p, q):
                    return True
        return False
    ans = []
    for w in words:
        if exist2(w):
            ans.append(w)
    return ans

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

print(findWords(board, words))
