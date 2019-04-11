import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return None
        dist = []
        heapq.heapify(dist)
        for x,y in points:
            heapq.heappush(dist, (x*x+y*y, x, y))
        res = []
        for i in range(K):
            res.append(heapq.heappop(dist)[1:])
        return res
