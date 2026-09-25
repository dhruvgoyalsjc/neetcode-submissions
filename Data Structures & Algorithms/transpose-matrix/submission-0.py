class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        res = [[0] * n for _ in range(m)]

        for r in range(n):
            for c in range(m):
                res[c][r] = matrix[r][c]

        return res