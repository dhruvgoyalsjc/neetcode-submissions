class Solution:
    def climbStairs(self, n: int) -> int:
        # let G(i) be number of ways to reach top starting from step i
        # G(i) = G(i+1) + G(i+2)
        # base case: i = n, 1 way (do nothing)
        # base case: i = n - 1, 1 way

        takeOneStep = 1
        takeTwoSteps = 1

        for i in range(n-2, -1, -1):
            temp = takeOneStep
            takeOneStep = takeOneStep + takeTwoSteps
            takeTwoSteps = temp

        return takeOneStep