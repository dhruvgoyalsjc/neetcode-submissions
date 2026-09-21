class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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