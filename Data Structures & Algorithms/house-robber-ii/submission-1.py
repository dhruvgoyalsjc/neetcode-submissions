class Solution:
    def rob(self, nums: List[int]) -> int:
        # two cases: either you rob from house 0 to n - 2
        # or from house 1 to n - 1. Just normal house robber for each case
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    
    # needs input array to be at least length two
    def helper(self, nums):
        n = len(nums)
        curr, next = nums[n - 1], 0
        for i in range(n - 2, -1, -1):
            newSum = max(nums[i] + next, curr)
            next = curr
            curr = newSum
        
        return curr
