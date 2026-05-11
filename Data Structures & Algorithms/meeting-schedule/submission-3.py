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

        # sort by start time
        intervals.sort(key=lambda i: i.start)

        # check if start time interferes with prev end time
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
            
        return True