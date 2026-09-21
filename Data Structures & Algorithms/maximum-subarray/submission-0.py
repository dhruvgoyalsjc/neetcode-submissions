class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(lo, hi) -> int:
            if lo == hi:
                return nums[lo]

            mid = (lo + hi) // 2

            leftSum = helper(lo, mid)
            rightSum = helper(mid + 1, hi)

            midSumLeft = currMidLeft = nums[mid]
            midSumRight = currMidRight = nums[mid + 1]

            for i in range(mid - 1, lo - 1, -1):
                currMidLeft += nums[i]
                midSumLeft = max(midSumLeft, currMidLeft)
            
            for i in range(mid + 2, hi + 1):
                currMidRight += nums[i]
                midSumRight = max(midSumRight, currMidRight)
            
            midSum = midSumLeft + midSumRight

            return max(leftSum, rightSum, midSum)
        
        return helper(0, len(nums) - 1)