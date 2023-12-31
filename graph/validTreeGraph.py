n = 5 
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

def validTree(n, edges):
    adj = [[] for _ in range(n)]
    seen = {}
    for s, d in edges:
        adj[s].append(d)
        adj[d].append(s)
    def dfs(node, prev):
        seen[node] = True
        for i in adj[node]:
            if i in seen:
                if i != prev:
                    return True
            else:
                if dfs(i, node):
                    return True
    
    if dfs(0, -1) or len(seen) != n:
        return False
    return True

print(validTree(n, edges))