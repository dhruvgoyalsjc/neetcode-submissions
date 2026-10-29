import sys
sys.setrecursionlimit(100000)

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adjList = defaultdict(list)
        for prevCourse, nextCourse in relations:
            adjList[prevCourse].append(nextCourse)
        
        # each node mapped to the max time to finish graph
        # from that node
        max_time = {}

        def dfs(src):
            if src in max_time:
                return max_time[src]
            
            months = 0
            for neighbor in adjList[src]:
                # first get max months from all possible 
                # future course paths
                months = max(months, dfs(neighbor))
            months += time[src - 1]

            max_time[src] = months
            return months

        for i in range(1, n + 1):
            dfs(i)

        return max(max_time.values())