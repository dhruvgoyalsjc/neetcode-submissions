class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        def makeFreqMap(s: str):
            mp = [0] * 26
            for c in s:
                mp[ord(c) - ord('a')] += 1
            return tuple(mp)
        

        for s in strs:
            anagrams[makeFreqMap(s)].append(s)
        
        return list(anagrams.values())