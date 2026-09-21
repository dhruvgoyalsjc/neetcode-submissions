class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
        
        # this solution is good but requires extra storage
        # for prefix and suffix arrays
        """
        n = len(nums)

        prefixArr = [1] * n
        suffixArr = [1] * n
        output = [1] * n

        prefixArr[0] = 1
        suffixArr[n-1] = 1

        for i in range(1, n):
            prefixArr[i] = prefixArr[i-1] * nums[i-1]
            suffixArr[n-i-1] = suffixArr[n-i] * nums[n-i]
            
        # after making prefix and suffix arr values we can
        # make the output value
        for i in range(n):
            output[i] = prefixArr[i] * suffixArr[i]

        return output
        """