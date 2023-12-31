n = 6
edges = [[0,1], [1,2], [2, 3], [4, 5]]

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, node):
        if node == self.par[node]:
            return node
        res = self.find(self.par[node])
        self.par[node] = res
        return res
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

def count_components(n, edges):
    uf = UnionFind(n)
    for n1, n2 in edges:
        if uf.union(n1, n2):
            n -= 1

    return n

print(count_components(n, edges))