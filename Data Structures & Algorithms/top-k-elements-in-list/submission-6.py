class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMp = Counter(nums)
        
        heap = []
        for num, freq in freqMp.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for _, num in heap]