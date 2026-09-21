class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        
        nextNextH = 0
        nextH = nums[n-1]

        for i in range(n - 2, -1, -1):
            ans = max(nums[i] + nextNextH, nextH)
            nextNextH = nextH
            nextH = ans
        
        # by end of loop nextH and ans always equal, 
        # also nextH is correct for base case of list is length 1
        return nextH