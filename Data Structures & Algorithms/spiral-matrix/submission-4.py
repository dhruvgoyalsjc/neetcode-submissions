class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        res = []

        t_border = -1
        b_border = n
        l_border = -1
        r_border = m
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        r = c = 0

        for i in range(m * n):
            res.append(matrix[r][c])

            dr, dc = directions[direction][0], directions[direction][1]

            if r + dr == t_border:
                l_border += 1
            elif r + dr == b_border:
                r_border -= 1
            elif c + dc == l_border:
                b_border -= 1
            elif c + dc == r_border:
                t_border += 1
            else:
                r += dr
                c += dc
                continue
            
            # change directions then continue
            direction = (direction + 1) % 4
            dr, dc = directions[direction][0], directions[direction][1]
            r += dr
            c += dc
        
        return res
        


