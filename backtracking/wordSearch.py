def exist(board, word):
    def dfs(i, row, col, visited):
        if (row<0 or col<0 or row>=len(board) or 
            col>=len(board[0]) or visited[row][col] or 
            board[row][col] != word[i]):
            return False
        visited[row][col] = True
        if i+1 == len(word):
            return True
        if (dfs(i+1, row-1, col, visited) or
            dfs(i+1, row, col+1, visited) or
            dfs(i+1, row+1, col, visited) or
            dfs(i+1, row, col-1, visited)):
            return True
        else:
            visited[row][col] = False
            return False
    p, q = 0, 0
    while p<len(board) or q < len(board[0]):
        visited = [[False]*len(board[0]) for _ in range(len(board))]
    
        if dfs(0, p, q, visited):
            return True
        else:
            if q<len(board[0]):
                q+=1
            else:
                p+=1
                q = 0
    return False

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print(exist(board, word))

# def exist2(board, word):
#     visited = [[False]*len(board[0]) for _ in range(len(board))]
#     def dfs(i, row, col):
#         if i == len(word):
#             return True
#         if (row<0 or col<0 or row>=len(board) or 
#             col>=len(board[0]) or visited[row][col] or 
#             board[row][col] != word[i]):
#             return False
#         visited[row][col] = True
#         res = (dfs(i+1, row-1, col) or
#             dfs(i+1, row, col+1) or
#             dfs(i+1, row+1, col) or
#             dfs(i+1, row, col-1))
#         visited[row][col] = False
#         return res
#     for p in range(len(board)):
#         for q in range(len(board[0])):
#             if dfs(0, p, q):
#                 return True
#     return False

# print(exist2(board, word))
