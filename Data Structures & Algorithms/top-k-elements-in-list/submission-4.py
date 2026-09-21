class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMp = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqMp.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res