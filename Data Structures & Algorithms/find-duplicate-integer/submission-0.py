class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if (slow == slow2):
                return slow
        
        # will never get to this point in the code anyway
        # return slow