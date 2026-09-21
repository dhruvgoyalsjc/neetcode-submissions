class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i: int, j: int) -> None:
            grid[i][j] = "0"
            
            if i > 0 and grid[i - 1][j] == "1": # up
                dfs(i - 1, j)
            if (j < len(grid[0]) - 1) and grid[i][j + 1] == "1": # right
                dfs(i, j + 1)
            if (i < len(grid) - 1) and grid[i + 1][j] == "1": # down
                dfs(i + 1, j)
            if j > 0 and grid[i][j - 1] == "1": # left
                dfs(i, j - 1)
        
        res = 0

        for i, row in enumerate(grid):
            for j, str in enumerate(row):
                if (str == "1"):
                    res += 1
                    dfs(i, j)
        
        return res