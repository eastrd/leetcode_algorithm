import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.h = nums
        heapq.heapify(self.h)
        while len(self.h) > k:
            heapq.heappop(self.h)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heapreplace(self.h, val)
        return self.h[0]
        
        
