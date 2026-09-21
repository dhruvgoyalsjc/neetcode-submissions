class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMp = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqMp.items():
            buckets[freq].append(num)
        
        res = []
        numLeft = k
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                res.append(num)
                numLeft -= 1
                if numLeft == 0:
                    return res
        
        # not needed but just here for completeness
        return res