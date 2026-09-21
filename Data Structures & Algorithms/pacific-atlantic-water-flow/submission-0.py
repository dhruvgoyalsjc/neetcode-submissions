class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        pacificSet = set()
        atlanticSet = set()

        # which set is 0 for pacific and 1 for atlantic
        def dfs(i, j, whichSet):
            if whichSet:
                currSet = atlanticSet
            else:
                currSet = pacificSet

            if (i, j) in currSet:
                return
            
            currSet.add((i, j))

            if i > 0 and heights[i - 1][j] >= heights[i][j]:
                dfs(i - 1, j, whichSet)
            if i < m - 1 and heights[i + 1][j] >= heights[i][j]:
                dfs(i + 1, j, whichSet)
            if j > 0 and heights[i][j - 1] >= heights[i][j]:
                dfs(i, j - 1, whichSet)
            if j < n - 1 and heights[i][j + 1] >= heights[i][j]:
                dfs(i, j + 1, whichSet)
        

        # now call dfs on the border cells
        for j in range(n):
            dfs(0, j, 0)
            dfs(m - 1, j, 1)
        
        for i in range(m):
            dfs(i, 0, 0)
            dfs(i, n - 1, 1)
        
        return list(pacificSet & atlanticSet)
    
