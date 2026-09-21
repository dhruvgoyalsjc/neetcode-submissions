class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        dp = [None] * len(nums)
        dp[len(nums) - 1] = 1

        for i in range(len(nums) - 1, -1, -1):
            if dp[i]:
                continue
            
            temp = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    temp = max(temp, 1 + dp[j])
            dp[i] = temp
            res = max(res, temp)
        
        return res