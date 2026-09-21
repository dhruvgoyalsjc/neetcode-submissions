class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # for first element x, max and min are initialized to x
        overallMax = nums[0]

        prevMax = nums[0]
        prevMin = nums[0]

        for i in range(1, len(nums)):
            tmp = nums[i] * prevMax
            prevMax = max(nums[i], tmp, nums[i] * prevMin)
            prevMin = min(nums[i], tmp, nums[i] * prevMin)
            overallMax = max(overallMax, prevMax)
        
        return overallMax