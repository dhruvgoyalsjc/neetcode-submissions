class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= m or nc >= n or 
                        grid[nr][nc] == '0'):
                        continue
                    # found another one
                    q.append((nr, nc))
                    # NOT RECURSIVE, need to set this to 0 in while loop
                    grid[nr][nc] = '0'

        numIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    numIslands += 1
        
        return numIslands
    

        