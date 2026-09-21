class TrieNode:
    def __init__(self, char):
        self.val = char
        self.children = defaultdict(TrieNode)
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        # go as deep as we possibly can before adding new nodes
        wordIndex = 0
        curr = self.root
        while (wordIndex < len(word) and 
                word[wordIndex] in curr.children):
            curr = curr.children[word[wordIndex]]
            wordIndex += 1
        
        # Now each new character that we process is being added
        while (wordIndex < len(word)):
            curr.children[word[wordIndex]] = TrieNode(word[wordIndex])
            curr = curr.children[word[wordIndex]]
            wordIndex += 1
        curr.isWord = True # finish the word

    def search(self, word: str) -> bool:
        wordIndex = 0
        curr = self.root
        while (wordIndex < len(word) and 
                word[wordIndex] in curr.children):
            curr = curr.children[word[wordIndex]]
            wordIndex += 1
        
        return (wordIndex == len(word) and curr.isWord)

    def startsWith(self, prefix: str) -> bool:
        wordIndex = 0
        curr = self.root
        while (wordIndex < len(prefix) and
                prefix[wordIndex] in curr.children):
            curr = curr.children[prefix[wordIndex]]
            wordIndex += 1

        return wordIndex == len(prefix)
        
        