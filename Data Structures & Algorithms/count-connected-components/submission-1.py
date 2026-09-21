class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # just do bfs and every time you need to call it again
        # from the main method just iterate

        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0]) # both ways since undirected

        discovered = [False] * n

        def bfs(src):
            q = deque([src])
            discovered[src] = True

            while (q):
                curr = q.popleft()
                for neighbor in adjList[curr]:
                    if not discovered[neighbor]:
                        discovered[neighbor] = True
                        q.append(neighbor)
        
        res = 0
        for i in range(n):
            if not discovered[i]:
                bfs(i)
                res += 1

        return res