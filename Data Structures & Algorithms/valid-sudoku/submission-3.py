class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        n = len(board)

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                if (num in rows[r] or
                    num in cols[c] or
                    num in squares[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                squares[(r // 3, c // 3)].add(num)
        return True
