def dfs(root, list):
    if not root: return
    if root.left: dfs(root.left, list)
    list.append(root.val)
    if root.right: dfs(root.right, list)
    return list

def isValidBST(root):
    list = dfs(root, [])
    for i in range(1, len(list)):
        if list[i-1] > list[i]:
            return False
    return True

def dfs2(root, greater, lesser):
    if not root: return True
    if lesser < root.val and greater > root.val:
        return (dfs2(root.left, root.val, lesser) and
                dfs2(root.right, greater, root.val))
    else: return False

def isValidBST2(root):
    if not root: return True
    return dfs2(root, float('int'), float('-inf'))
