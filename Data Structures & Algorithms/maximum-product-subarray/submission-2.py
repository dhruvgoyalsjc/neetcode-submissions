class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # for first element x, max and min are initialized to x
        overallMax = nums[0]

        prevMax = nums[0]
        prevMin = nums[0]

        for i in range(1, len(nums)):
            currMax = max(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            currMin = min(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            overallMax = max(overallMax, currMax)
            prevMax = currMax
            prevMin = currMin
        
        return overallMax