class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        mid = (lo + hi) // 2

        while (lo <= hi):
            if nums[mid] > nums[hi]:
                # min is for sure to right of mid
                # min is also for sure not at mid itself
                lo = mid + 1
                mid = (lo + hi) // 2
            elif nums[mid] < nums[hi]:
                # min is for sure to right of mid
                # min could potench be mid itself
                hi = mid
                mid = (lo + hi) // 2
            else:
                return nums[mid]