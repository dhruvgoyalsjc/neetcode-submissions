class Solution:

    def encode(self, strs: List[str]) -> str:
        tempLst = []
        for s in strs:
            tempLst.append(str(len(s)))
            tempLst.append("#")
            tempLst.append(s)
        print("".join(tempLst))
        return "".join(tempLst)

    def decode(self, s: str) -> List[str]:
        res = []

        startOfNum = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                i += 1
                continue
            if s[i] == "#":
                lenStr = int(s[startOfNum: i])
                res.append(s[i + 1: i + 1 + lenStr])
            startOfNum = i + 1 + lenStr
            i = startOfNum
        
        return res
