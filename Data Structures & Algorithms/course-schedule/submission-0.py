class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        # make the adjacency list
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])

        greyNodes = set()
        discovered = set()
        
        self.isCycle = False

        def dfs(currCourse: int):
            if currCourse in greyNodes:
                self.isCycle = True
                return
            if currCourse in discovered:
                return
            
            greyNodes.add(currCourse)
            discovered.add(currCourse)

            for neighbor in adj[currCourse]:
                dfs(neighbor)
            
            greyNodes.remove(currCourse)

        for i in range(numCourses):
            dfs(i)
        
        return not self.isCycle