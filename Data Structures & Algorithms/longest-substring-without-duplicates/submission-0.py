class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        l = 0
        res = 0
        seen = {} # map from char to latest index it was seen

        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            
            seen[s[r]] = r 
            res = max(res, r - l + 1)
        
        return res