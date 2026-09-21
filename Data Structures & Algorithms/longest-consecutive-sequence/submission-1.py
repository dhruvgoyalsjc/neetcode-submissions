class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        numsSet = set(nums)
        res = 1

        for num in numsSet:
            if (num - 1) not in numsSet:
                seqLen = 1
                while ((num + 1) in numsSet):
                    seqLen += 1
                    num += 1
                
                if seqLen >= res:
                    res = seqLen
        
        return res