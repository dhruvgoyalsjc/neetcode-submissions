class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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