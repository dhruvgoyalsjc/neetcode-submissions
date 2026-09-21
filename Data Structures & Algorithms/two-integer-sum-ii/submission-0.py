class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        res = []

        l, r = 0, n-1

        while (l < r):
            if numbers[l] + numbers[r] == target:
                l += 1
                r += 1
                res.append(l)
                res.append(r)
                return res
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        
        return res