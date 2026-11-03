class Solution:
    # helper dfs method
    def dfs(self, curr: int, greyNodes, discovered, blackNodes, adjList) -> bool:
        if greyNodes[curr]:
            return False
        if discovered[curr]:
            return True

        discovered[curr] = True
        greyNodes[curr] = True

        for neighbor in adjList[curr]:
            if not self.dfs(neighbor, greyNodes, discovered, blackNodes, adjList): 
                # return False if we run into cycle in future
                return False
            
        # dfs successfully finished
        greyNodes[curr] = False
        blackNodes.append(curr)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:    
        # first make adjacency list
        adjList = defaultdict(list)
        for prereq in prerequisites:
            adjList[prereq[1]].append(prereq[0])

        # topo sort by returning reverse finish time for DFS
        # essentially add nodes to blackNodes as they finish and return blackNodes reversed
        greyNodes = [False] * numCourses
        discovered = [False] * numCourses
        blackNodes = []

        for i in range(numCourses):    
            if not self.dfs(i, greyNodes, discovered, blackNodes, adjList):
                return [] # empty return if toposort not possible
        
        res = blackNodes[::-1]
        return res
    