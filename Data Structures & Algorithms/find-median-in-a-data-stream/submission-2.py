class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # contains first half of array
        self.minHeap = [] # contains second half of array

    def addNum(self, num: int) -> None:
        # case where minHeap is empty
        if not self.minHeap:
            heapq.heappush(self.minHeap, num)
            return
        
        # minHeap not empty, compare to minHeap
        if num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            # need to keep negative values for maxheap
            heapq.heappush(self.maxHeap, -num)

        # rebalance if needed
        if len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, 
                -1 * heapq.heappop(self.minHeap))
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, 
                -1 * heapq.heappop(self.maxHeap))


    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return (-1 * self.maxHeap[0])
        else:
            return float(self.minHeap[0] + (-1 * self.maxHeap[0])) / 2
        
        