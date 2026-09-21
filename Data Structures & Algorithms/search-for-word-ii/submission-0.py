class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

    def add(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        
        curr.isWord = True

    # def search(self, word):
    #     curr = self.root

    #     for c in word:
    #         if c not in curr.children:
    #             return False
    #         curr = curr.children[c]
        
    #     return curr.isWord
    
    # def searchPrefix(self, prefix):
    #     curr = self.root

    #     for c in word:
    #         if c not in curr.children:
    #             return False
    #         curr = curr.children[c]
        
    #     return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # initialize trie with all words in list
        trie = TrieNode()
        for word in words:
            trie.add(word)
        
        m, n = len(board), len(board[0])
        
        res = set()

        def dfs(i, j, node, word):
            if (i < 0 or j < 0 or i >= m or j >= n or
                board[i][j] == '#' or board[i][j] not in node.children):
                return
            
            # mark cell as visited
            temp = board[i][j]
            board[i][j] = '#'

            word += temp
            node = node.children[temp]
            # check if we found anything in our list
            if node.isWord:
                res.add(word)
            
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)

            # undo marking the board as visited
            board[i][j] = temp


        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")

        return list(res)