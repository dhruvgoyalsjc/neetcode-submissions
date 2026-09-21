class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time, remove the overlapping interval with larger end time
        intervals.sort(key = lambda i: i[1])

        numRemoved = 0
        prevEndTime = intervals[0][1]

        for interval in intervals[1:]:
            start, end = interval
            if (prevEndTime <= start):
                prevEndTime = end
            else:
                numRemoved += 1
        
        return numRemoved