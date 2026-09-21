class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build a graph from the relationships you know
        # each letter is a node, a -> b means a < b

        # make sure all letters initialized to an empty set
        adjList = {c: set() for word in words for c in word}

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

        # topo sort the graph and return topo-sorted order
        res = []
        visited = {} # value is false if unfinished, true if finished
        finished = set()
        
        def dfs(curr):
            if curr in visited:
                return visited[curr]
            
            visited[curr] = False

            for neighbor in adjList[curr]:
                if not dfs(neighbor):
                    return False
            
            # now we just finished, so add to front of res
            visited[curr] = True
            res.insert(0, curr)

            return True
        
        for c in adjList:
            if c not in visited:
                if not dfs(c):
                    return ""

        return "".join(res)