class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # most efficient solution is to use 3 bitmaps, each elem is 9 bits
        n = len(board)
        rows = [0] * n
        cols = [0] * n
        squares = [0] * n

        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == ".":
                    continue
                
                # to turn 1-9 into 0-8 so that indexable into bitmap
                val = int(elem) - 1
                # to identify which 3x3 square
                squareIndex = (i // 3) * 3 + (j // 3)

                if (1 << val & rows[i] or 
                    1 << val & cols[j] or
                    1 << val & squares[squareIndex]):
                    return False

                rows[i] |= 1 << val
                cols[j] |= 1 << val
                squares[squareIndex] |= 1 << val
        
        return True

        '''
        # This is the hashset solution (there is a better soln with only n storage)
        rowHashSet = defaultdict(set)
        colHashSet = defaultdict(set)
        squareHashSet = defaultdict(set)
        
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == ".":
                    continue                
                if (elem in rowHashSet[i] or 
                    elem in colHashSet[j] or 
                    elem in squareHashSet[(i // 3, j // 3)]):
                    return False
                
                rowHashSet[i].add(elem)
                colHashSet[j].add(elem)
                squareHashSet[(i // 3, j // 3)].add(elem)
        
        return True
        '''