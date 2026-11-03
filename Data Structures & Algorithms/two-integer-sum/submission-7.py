class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToIndex = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in valToIndex:
                return [valToIndex[diff], i]
            valToIndex[nums[i]] = i
        