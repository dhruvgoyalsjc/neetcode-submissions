class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # map from index to the product of all elements after that index
        mp = {}
        product = 1
        mp[len(nums) - 1] = 1

        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            mp[i] = product
        
        res = [0] * len(nums)
        prevProduct = 1

        for i in range(0, len(nums)):
            res[i] = prevProduct * mp[i]
            prevProduct *= nums[i]
        
        return res