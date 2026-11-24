class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def add(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.isWord = True
    
    def remove(self, word):
        curr = self

        parents_and_children = []
        for c in word:
            parents_and_children.append((curr, c))
            curr = curr.children[c]
        
        for parent, child_key in reversed(parents_and_children):
            target = parent.children[child_key]

            if len(target.children) == 0:
                del parent.children[child_key]
            else:
                return # cant remove anything else from trie path

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.add(word)
        
        m, n = len(board), len(board[0])

        res = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= m or c >= n or
                board[r][c] == "#" or
                board[r][c] not in node.children):
                return
        
            temp = board[r][c] # assert temp is in node.children
            # mark cell visited so we don't see it again in same word
            board[r][c] = "#" 

            word += temp
            node = node.children[temp]
            if node.isWord:
                res.add(word)
                trie.remove(word)
            
            # recurse in 4 directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # unmark cell as visited to allow backtracking
            board[r][c] = temp
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")
        
        return list(res)