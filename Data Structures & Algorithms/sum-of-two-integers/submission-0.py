class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF

        while b:
            temp = (a & b) << 1
            a = (a ^ b) & mask
            b = temp & mask
        return a if a <= maxInt else ~(a ^ mask)