# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        vals = data.split(',')
        self.i = 0
        def dfs():
            if vals[self.i] == 'N':
                self.i+=1
                return None
            root = TreeNode(int(vals[self.i]))
            self.i+=1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
