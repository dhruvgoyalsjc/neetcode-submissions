class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start time
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]

        for i in range (1, len(intervals)):
            # if curr intervals start is before 
            #last added interval's end date
            if (intervals[i][0] <= res[-1][1]):
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res