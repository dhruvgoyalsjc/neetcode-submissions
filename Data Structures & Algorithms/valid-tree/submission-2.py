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

        def dfs(node, prev):
            if node in discovered:
                return False
            
            discovered.add(node)

            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        return dfs(0, None) and (len(discovered) == n)