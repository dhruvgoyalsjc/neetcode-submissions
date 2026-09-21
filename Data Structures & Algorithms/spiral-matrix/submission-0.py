class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        res = []
        r = c = 0
        LBorder = -1
        RBorder = n
        UBorder = -1
        DBorder = m

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direct = 0
        dr, dc = directions[direct][0], directions[direct][1]
        
        for i in range(m * n):
            res.append(matrix[r][c])

            dr, dc = directions[direct][0], directions[direct][1]

            if (r + dr == UBorder):
                LBorder += 1
            elif (r + dr == DBorder):
                RBorder -= 1
            elif (c + dc == LBorder):
                DBorder -= 1
            elif (c + dc  == RBorder):
                UBorder += 1
            else:
                r += dr
                c += dc
                continue
            
            # change directions and then continue
            direct = (direct + 1) % 4
            dr, dc = directions[direct][0], directions[direct][1]
            r += dr
            c += dc
        
        return res