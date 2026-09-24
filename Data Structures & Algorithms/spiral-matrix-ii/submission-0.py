class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]

        t_border = -1
        l_border = -1
        b_border = n
        r_border = n

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direct = 0

        r = c = 0
        for i in range(n * n):
            res[r][c] = i + 1

            dr, dc = directions[direct][0], directions[direct][1]
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
            
            # change direction case
            direct = (direct + 1) % 4
            dr, dc = directions[direct][0], directions[direct][1]
            r += dr
            c += dc
        
        return res

            