from collections import deque

def maxDepth2(root):
    if not root: return 0
    queue = deque([root])
    level = 0
    while queue:
        level+=1
        lenOfQueue = len(queue)
        for _ in range(lenOfQueue):
            popped = queue.popleft()
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
    return level

def maxDepth(root):
    if not root: return 0
    return 1+max(maxDepth(root.left), maxDepth(root.right))
