class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        # transpose matrix
        for r in range(n):
            for c in range(r, m):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        
        # then horizontally reverse matrix
        for r in range(n):
            matrix[r].reverse()