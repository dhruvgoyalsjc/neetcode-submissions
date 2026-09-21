class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charFreqS = defaultdict(int)
        charFreqT = defaultdict(int)

        for c in s:
            charFreqS[c] += 1
        
        for c in t:
            charFreqT[c] += 1
        
        return charFreqS == charFreqT