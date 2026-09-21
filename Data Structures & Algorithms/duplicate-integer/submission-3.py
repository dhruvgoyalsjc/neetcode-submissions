class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        
        # s = set()
        # for num in nums:
        #     if num in s:
        #         return True
        #     s.add(num)
        # return False