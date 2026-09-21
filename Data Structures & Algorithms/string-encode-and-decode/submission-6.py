class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for str in strs:
            encoding = f"{len(str)}#{str}"
            res += encoding

        return res 

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        startOfEncoding = 0
        while i < len(s):
            if s[i] == '#':
                strlen = int(s[startOfEncoding: i])
                str = s[i+1: i+strlen+1]
                res.append(str)
                i += strlen
                startOfEncoding = i+1
            i += 1

        return res

        '''
        POOR ATTEMPT AT USING FOR LOOP:

        startOfEncoding = 0
        for i, char in enumerate(s):
            if char == '#':
                strlen = int(s[startOfEncoding: i])
                str = s[i+1: i+strlen+1]
                res.append(str)
                print(res)
                i += strlen
                startOfEncoding = i+1

        return res
        '''