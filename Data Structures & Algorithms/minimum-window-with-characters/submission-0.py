class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # quick edge cases
        if t == "": return ""
        if len(s) < len(t):
            return ""

        # declare maps we care about
        cntT = Counter(t)
        cntS = {}

        have, need = 0, len(cntT)
        
        # for current window
        l, r = 0, 0
        # for best window
        minL, minR, minLen = -1, len(s), float("infinity")

        for r in range(len(s)):
            if s[r] in cntT:
                cntS[s[r]] = cntS.get(s[r], 0) + 1
                if cntS[s[r]] == cntT[s[r]]:
                    have += 1

            while (have == need):
                if (r - l + 1) < (minLen):
                    minL = l
                    minR = r
                    minLen = r - l + 1
                if (s[l] in cntT):
                    cntS[s[l]] -= 1
                    if (cntS[s[l]] < cntT[s[l]]):
                        have -= 1
                l += 1
        
        if minLen == float("infinity"):
            return ""
        return s[minL: minR + 1]