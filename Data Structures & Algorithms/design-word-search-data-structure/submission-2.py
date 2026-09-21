class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(curr, i) -> bool:
            if i == len(word):
                return curr.isWord
            
            c = word[i]

            if c == '.':
                # in the case where c == '.', recursively search all child paths
                for child in curr.children.values():
                    if dfs(child, i + 1):
                        return True
                    # no child path worked, thus will go to false
            else:
                if c in curr.children:
                    return dfs(curr.children[c], i + 1)
            return False
        
        return dfs(self.root, 0)