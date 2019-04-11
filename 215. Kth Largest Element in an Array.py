from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Brute force: sort then count -> O(NlogN + some N)
        # Heap approach: Truncate the min heap size to k, then add elements in
        #   -> O(NlogN)
        if not nums:
            return None
        res = []
        for i in nums:
            heappush(res, i)
            while len(res) > k:
                heappop(res)
        return res[0]
