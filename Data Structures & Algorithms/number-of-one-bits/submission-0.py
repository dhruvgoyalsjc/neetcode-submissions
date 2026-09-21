class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        res = 0
        for i in range(32):
            if n & mask:
                res += 1
            mask <<= 1

        return res