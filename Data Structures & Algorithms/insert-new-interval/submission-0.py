class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        
        res = []

        for i in range(len(intervals)):
            interval = intervals[i]
            start, end = interval
            
            if (end < newStart):
                # if before interval to add then add
                res.append(interval)
            elif (start > newEnd):
                # this interval is after the interval to add
                res.append([newStart, newEnd])
                return res + intervals[i: ]
            else: # case of overlapping intervals
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)
        
        # if we got here int the code then we never added new interval to res
        res.append([newStart, newEnd])
        return res
            
