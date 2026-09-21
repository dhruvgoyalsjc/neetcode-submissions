class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n: 1}
        dp[n - 1] = 1 if s[n - 1] != '0' else 0

        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            elif s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456"):
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]

        return dp[0]