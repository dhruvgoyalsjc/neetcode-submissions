"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        intervals.sort(key = lambda i: i.start) # sort by start time

        prevEndTime = intervals[0].end
        for interval in intervals[1: ]:
            if interval.start < prevEndTime:
                return False
            prevEndTime = interval.end

        return True
