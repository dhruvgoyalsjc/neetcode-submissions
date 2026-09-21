class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = the max amount you can rob from house i onwards
        n = len(nums)
        dp = [0] * (n+1)
        dp[n] = 0
        dp[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        
        return dp[0]