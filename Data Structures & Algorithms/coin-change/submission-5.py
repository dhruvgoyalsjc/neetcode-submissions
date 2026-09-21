class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None for _ in range(amount + 1)]
        def recHelper(amount):
            if amount < 0:
                return float("inf")
            if amount == 0:
                return 0
            if dp[amount]:
                return dp[amount]
            
            minNumCoins = float("inf")
            for coin in coins:
                minNumCoins = min(minNumCoins, 1 + recHelper(amount - coin))
            dp[amount] = minNumCoins
            return minNumCoins

        res = recHelper(amount)
        if res == float("inf"):
            return -1
        else:
            return res
                