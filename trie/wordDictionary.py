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

    def search(self, word: str) -> bool:
        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                if word[i] == '.':
                    for n in curr.child.values():
                        if dfs(i+1, n):
                            return True
                    return False
                else:
                    if word[i] not in curr.child:
                        return False
                    curr = curr.child[word[i]]
            return curr.word
        return dfs(0, self.root)
    
w = WordDictionary()
w.addWord('a')
w.addWord('a')
w.search('.')
w.search('a')
w.search('aa')
w.search('a')
w.search('a.')
w.search('.a')