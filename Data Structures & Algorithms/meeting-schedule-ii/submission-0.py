"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # min num diff days = max num overlaps
        # count num intervals active at a specific time
        # each time an interval starts, increase cnt
        # each time interval ends, decrease cnt
        n = len(intervals)
        intervals.sort(key = lambda x: x.start)

        endSorted = intervals.copy()
        endSorted.sort(key = lambda x: x.end)

        i, j = 0, 0
        maxNum = 0
        currNum = 0
        while (i < n and j < n):
            if intervals[i].start < endSorted[j].end:
                i += 1
                currNum += 1
            else:
                j += 1
                currNum -= 1
            maxNum = max(maxNum, currNum)

        return maxNum