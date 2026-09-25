class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        # transpose matrix
        for r in range(n):
            for c in range(r, m):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # then horizontally reverse matrix
        for row in matrix:
            row.reverse()