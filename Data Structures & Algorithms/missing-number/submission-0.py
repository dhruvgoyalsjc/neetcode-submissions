class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (int) ((1 + n) * n / 2) - sum(nums)