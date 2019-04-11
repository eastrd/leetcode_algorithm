# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda i: i.start)
        mins = []
        heapq.heapify(mins)
        rooms = 0
        for i in intervals:
            s, e = i.start, i.end
            if rooms == 0:
                heapq.heappush(mins, e)
                rooms += 1
                continue
            if s < mins[0]:
                rooms += 1
            else:
                heapq.heappop(mins)
            heapq.heappush(mins, e)
        return rooms
