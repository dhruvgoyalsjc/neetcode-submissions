class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        firstRowZero = False

        # set top row to denote if their col should be zero'd
        # leftmost col to denote if their row should be zero'd
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        firstRowZero = True
                    else:
                        matrix[i][0] = 0
        

        # check each positions's row and coln and zero it if needed
        for i in range(1, m):
            for j in range(1, n):
                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
        
        # zero out first col if needed
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
                
        # at the END zero out the first row if needed
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
