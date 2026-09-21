class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        # make adj List
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        discovered = set()

        def dfs(node):
            if node in discovered:
                return
            
            discovered.add(node)

            for neighbor in adjList[node]:
                dfs(neighbor)

        dfs(0)
        
        return (len(discovered) == n) 