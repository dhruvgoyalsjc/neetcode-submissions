class Solution:
    def rob(self, nums: List[int]) -> int:
        # two cases: either you rob from house 0 to n - 2
        # or from house 1 to n - 1. Just normal house robber for each case
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        # Case 1:
        sum = 0
        next = 0
        curr = nums[n - 2]

        for i in range(n - 3, -1, -1):
            temp = max(nums[i] + next, curr)
            next = curr
            curr = temp
        
        # curr is the value we want

        # Case 2:
        sum = 0
        next = 0
        curr2 = nums[n - 1]

        for i in range(n - 2, 0, -1):
            temp = max(nums[i] + next, curr2)
            next = curr2
            curr2 = temp
        
        return max(curr, curr2)