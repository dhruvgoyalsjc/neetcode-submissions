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
        curr = self.root

        def searchRecursive(curr, wordSubstring) -> bool:
            if wordSubstring == "" and curr.isWord:
                return True

            for i in range(len(wordSubstring)):
                c = wordSubstring[i]

                if c not in curr.children:
                    if c != '.':
                        return False
                    # in the case where c == '.', recursively
                    # search all child paths
                    for child in curr.children:
                        if searchRecursive(curr.children[child], 
                        wordSubstring[i + 1:]):
                            return True
                    # no child path worked, thus false
                    return False
                else:
                    curr = curr.children[c]
            
            return curr.isWord
        
        return searchRecursive(curr, word)
