class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def inBounds(i, j):
            return (0 <= i < len(board) and 0 <= j < len(board[0]))

        def dfs(i, j, wordIndex):
            if wordIndex >= len(word):
                return True
            
            if not inBounds(i, j):
                return False
            if board[i][j] != word[wordIndex] or board[i][j] == "#":
                return False
            
            board[i][j] = "#"
            res = (dfs(i + 1, j, wordIndex + 1) or
                dfs(i - 1, j, wordIndex + 1) or
                dfs(i, j + 1, wordIndex + 1) or
                dfs(i, j - 1, wordIndex + 1))
            board[i][j] = word[wordIndex]
            return res
        
        wordCnt = collections.Counter(word)
        boardCnt = collections.Counter(c for row in board for c in row)

        # optimization to help us short circuit if we can
        for c in wordCnt:
            if wordCnt[c] > boardCnt[c]:
                return False
        
         # start from the rarer letter to avoid doing dfs as much as possible
        if boardCnt[word[0]] > boardCnt[word[-1]]:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False
