class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(i: int, j: int) -> None:
            if (i < 0 or j < 0 or 
                i >= len(grid) or j >= len(grid[0]) 
                or grid[i][j] == "0"
            ):
                return
            
            grid[i][j] = "0"
            for direction in directions:
                dfs(i + direction[0], j + direction[1])
        
        res = 0
        for i, row in enumerate(grid):
            for j, str in enumerate(row):
                if (str == "1"):
                    res += 1
                    dfs(i, j)
        return res