class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        mid = (lo + hi) // 2

        while (lo <= hi):
            if (target < nums[mid]):
                hi = mid - 1
                mid = (lo + hi) // 2
            elif (target > nums[mid]):
                lo = mid + 1
                mid = (lo + hi) // 2
            else:
                return mid
        
        return -1