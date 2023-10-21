from collections import deque

def levelOrder(root):
    res = []
    q = deque()
    if root:
        q.append(root)
    while q:
        ans = []
        for _ in range(len(q)):
            p = q.popleft()
            ans.append(p.val)
            if p.left: q.append(p.left)
            if p.right: q.append(p.right)
        res.append(ans)
    return res
