class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        if (n == 1):
            return [[nums[0]]]

        res = []

        for i in range(n):
            nums[i], nums[n-1] = nums[n-1], nums[i]
            remainingLists = self.permute(nums[:n - 1])
            for item in remainingLists:
                item.append(nums[n-1])
                res.append(item)
            nums[i], nums[n-1] = nums[n-1], nums[i]

        return res