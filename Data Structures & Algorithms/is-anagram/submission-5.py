class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqS = Counter(s)
        freqT = Counter(t)

        return freqS == freqT