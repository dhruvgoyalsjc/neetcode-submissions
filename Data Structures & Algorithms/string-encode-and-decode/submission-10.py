class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        
        startOfNum = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                i += 1
                continue
            if s[i] == "#":
                strLen = int(s[startOfNum: i])
                res.append(s[i + 1: i + 1 + strLen])
                startOfNum = i + 1 + strLen
                i = startOfNum
        
        return res
