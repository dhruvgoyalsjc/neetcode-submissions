class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1] * n

        for i in range(m - 1): # because first row done, so m-1 rows left to process
            currRow = [1] * n
            for j in range(n - 2, -1, -1): 
                # already know currRow[n-1] = 1, so this avoids out of bounds checks
                currRow[j] = currRow[j + 1] + prevRow[j]
            prevRow = currRow
        
        return prevRow[0]