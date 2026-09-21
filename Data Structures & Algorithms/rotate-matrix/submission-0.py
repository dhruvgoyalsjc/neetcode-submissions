class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reverseHorizontal(matrix)
        
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reverseHorizontal(self, matrix):
        for row in matrix:
            row.reverse()