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
        def searchRecursive(curr, j) -> bool:
            if j == len(word) and curr.isWord:
                return True

            for i in range(j, len(word)):
                c = word[i]

                if c not in curr.children:
                    if c != '.':
                        return False
                    # in the case where c == '.', recursively
                    # search all child paths
                    for child in curr.children.values():
                        if searchRecursive(child, i + 1):
                            return True
                    # no child path worked, thus false
                    return False
                else:
                    curr = curr.children[c]
            
            return curr.isWord
        
        return searchRecursive(self.root, 0)
