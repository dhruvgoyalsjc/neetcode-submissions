class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        nums.sort()
        
        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if i > 0 and num == nums[i - 1]:
                continue

            target = 0 - num
            l, r = i + 1, n - 1
            while (l < r):
                if nums[l] + nums[r] == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        
        return res
