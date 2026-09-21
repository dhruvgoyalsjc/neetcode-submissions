class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def permuteRec(start: int):
            if (start == n):
                res.append(nums[:])
            
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                permuteRec(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        permuteRec(0)
        return res