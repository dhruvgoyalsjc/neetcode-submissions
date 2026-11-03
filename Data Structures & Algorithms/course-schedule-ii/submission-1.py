class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # make an adjacency list
        adjList = defaultdict(list)
        for nxt, prev in prerequisites:
            adjList[prev].append(nxt)
        
        discovered, grey_nodes = set(), set()
        finished = []

        def dfs(src):
            if src in grey_nodes:
                return False
            if src in discovered:
                return True
            
            discovered.add(src)
            grey_nodes.add(src)

            for neighbor in adjList[src]:
                if not dfs(neighbor):
                    return False
            
            grey_nodes.remove(src)
            finished.append(src)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return finished[::-1]