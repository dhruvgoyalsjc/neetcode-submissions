class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in numSet:
            currLen = 0
            if (num - 1) not in numSet:
                while (num + currLen) in numSet:
                    currLen += 1
                res = max(res, currLen)
        
        return res
