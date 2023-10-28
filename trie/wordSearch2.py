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

class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.word = True

def findWords2(board, words):
    ans = set()
    def dfs(node, r, c, res):
        if (r<0 or c<0 or r>=len(board) or c>=len(board[0]) or
            board[r][c] == '#' or board[r][c] not in node.child):
            return
        tmp = board[r][c]
        res += board[r][c]
        node = node.child[tmp]
        if node.word: ans.add(res)
        board[r][c] = '#'
        dfs(node, r+1, c, res)
        dfs(node, r-1, c, res)
        dfs(node, r, c+1, res)
        dfs(node, r, c-1, res)
        board[r][c] = tmp
    trie = WordDictionary()
    for n in words:
        trie.addWord(n)
    for r in range(len(board)):
        for c in range(len(board[0])):
            dfs(trie.root, r, c, '')
    return list(ans)

print(findWords2(board, words))
