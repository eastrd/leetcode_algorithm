from heapq import *
 
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l, self.u = [], []
        
    def addNum(self, num: int) -> None:
        heappush(self.u, -heappushpop(self.l, -num))
        if len(self.u) > len(self.l):
            heappush(self.l, -heappop(self.u))
        
    def findMedian(self) -> float:
        if len(self.l) > len(self.u):
            return -self.l[0]
        return (self.u[0] - self.l[0]) / 2 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
