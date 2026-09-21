class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build a graph from the relationships you know
        # each letter is a node, a -> b means a < b

        adjList = {}

        for word in words:
            for c in word:
                if c not in adjList:
                    adjList[c] = set()

        for i in range(len(words) - 1):
            firstDiff = 0
            while firstDiff < len(words[i]):
                if firstDiff >= len(words[i + 1]):
                    return "" # this means impossible case
                
                c1, c2 = words[i][firstDiff], words[i + 1][firstDiff]
                if (c1 != c2):
                    adjList[c1].add(c2)
                    break

                firstDiff += 1

        # topo sort the graph and return ur topo-sorted order
        res = []
        visited = set()
        finished = set()
        
        def dfs(curr):
            if curr in finished:
                return True
            if curr in visited:
                return False
            
            visited.add(curr)

            for neighbor in adjList[curr]:
                if not dfs(neighbor):
                    return False
            
            # now we just finished, so add to front of res
            finished.add(curr)
            res.insert(0, curr)

            return True
        
        for c in adjList:
            if c not in visited:
                if not dfs(c):
                    return ""

        return "".join(res)