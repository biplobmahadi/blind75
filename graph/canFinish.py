from collections import deque

# naive
def canFinish(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]
    for d, s in prerequisites:
        adj[s].append(d)
    
    def bfs(node):
        seen = set()
        seen.add(node)
        q = deque()
        q.append(node)
        while q:
            p = q.popleft()
            for n in adj[p]:
                if n == node:
                    return True
                if n not in seen:
                    seen.add(n)
                    q.append(n)
        return False
    
    for i in range(numCourses):
        if bfs(i):
            return False
    return True

n = 6
pre = [[1, 0], [2, 1], [5, 2], [0, 3], [4, 3], [3, 5], [4, 5]]

print(canFinish(n, pre))

def canFinishOptimal(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for d, s in prerequisites:
        adj[s].append(d)
        indegree[d] += 1
    s = []
    for i, n in enumerate(indegree):
        if n == 0:
            s.append(i)
    count = 0
    while s:
        p = s.pop()
        count+=1
        for node in adj[p]:
            indegree[node] -= 1
            if indegree[node] == 0:
                s.append(node)

    return count == numCourses

print(canFinishOptimal(n, pre))