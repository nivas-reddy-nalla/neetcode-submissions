"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval:interval.start)

        n = len(intervals)
        if n<=1:
            return True
        prev = intervals[0]

        for i in range(1, n):
            cur = intervals[i]
            if cur.start<prev.end:
                return False
            prev = cur
        
        return True
