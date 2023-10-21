def maxPathSum(root):
    res = [root.val]
    def dfs(root):
        if not root: return 0
        leftMax = max(0, dfs(root.left))
        rightMax = max(0, dfs(root.right))
        res[0] = max(res[0], leftMax+rightMax+root.val)
        return max(leftMax, rightMax) + root.val
    dfs(root)
    return res[0]
