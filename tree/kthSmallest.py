def dfs(root, list):
    if not root: return
    if root.left: dfs(root.left, list)
    list.append(root.val)
    if root.right: dfs(root.right, list)
    return list

def kthSmallest(root, k):
    list = dfs(root, [])
    return list[k-1]