"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        res = 0
        i = 0
        intervals.sort(key=lambda x:x.start)
        while i < len(intervals):
            while heap and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            res = max(len(heap), res)
            i += 1
        return res