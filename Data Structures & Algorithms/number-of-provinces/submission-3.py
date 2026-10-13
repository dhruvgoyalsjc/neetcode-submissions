class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.numSets = n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset: # already same parent/set
            return
        self.numSets -= 1
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[yset] < self.rank[xset]:
            self.parent[yset] = xset
        else: # ranks are same
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i):
                if isConnected[i][j]:
                    uf.union(i, j)
        
        return uf.numSets

