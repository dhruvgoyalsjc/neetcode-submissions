from bisect import bisect_left

class Solution:
    def __init__(self, w: List[int]):
        self.prefixSum = [w[0]]
        for i in range(1, len(w)):
            self.prefixSum.append(self.prefixSum[-1] + w[i])

        self.total = self.prefixSum[-1]

    def pickIndex(self) -> int:
        # rand is between [0.0, 1.0)
        randNum = random.random() * self.total

        return bisect_left(self.prefixSum, randNum)

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()