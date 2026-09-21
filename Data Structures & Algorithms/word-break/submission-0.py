class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordLens = defaultdict(list)
        for word in wordDict:
            wordLens[len(word)].append(word)

        dp = [None] * (len(s) + 1)
        dp[len(s)] = True

        def recHelper(i):
            if dp[i] is not None:
                return dp[i]
        
            for wordLen in wordLens:
                if i + wordLen <= len(s) and s[i: i + wordLen] in wordLens[wordLen]:
                    if recHelper(i + wordLen):
                        dp[i] = True
                        return True
            
            dp[i] = False
            return False
        
        return recHelper(0)