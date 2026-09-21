class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        mid = (lo + hi) // 2

        k = 0

        
        if (nums[lo] == target):
            return lo
        elif (nums[hi] == target):
            return hi
        

        # trying to find the position of the minimum element
        while (lo <= hi):
            if (nums[mid] == target):
                return mid

            if (nums[mid] > nums[hi]):
                lo = mid + 1 # for sure mid cannot be the minimum element so we can exclude
                mid = (lo + hi) // 2
            elif (nums[mid] < nums[hi]):
                hi = mid
                mid = (lo + hi) // 2
            else:
                k = mid
                break

        # INVARIANT: we know k is the pivot index
        
        # remember to reset lo, hi
        lo, hi = 0, len(nums) - 1

        if (nums[k] <= target and target <= nums[hi]):
            lo = k
        else:
            hi = k - 1
        
        # now calculate mid once we found the right lo and hi bounds
        mid = (lo + hi) // 2
        
        while (lo <= hi):
            if (target > nums[mid]):
                lo = mid + 1
                mid = (lo + hi) // 2
            elif (target < nums[mid]):
                hi = mid - 1
                mid = (lo + hi) // 2
            else:
                return mid
        
        return -1