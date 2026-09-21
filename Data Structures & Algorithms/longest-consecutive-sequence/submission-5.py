class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)

        res = 1

        for num in numSet:
            currLen = 1
            if (num - 1) in numSet:
                continue
            else:
                while (num + 1) in numSet:
                    num += 1
                    currLen += 1
                res = max(res, currLen)
        
        return res
