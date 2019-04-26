class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)
        for s, e in intervals:
            if res and s <= res[-1][1]:
                res[-1] = [res[-1][0], max(e, res[-1][1])]
            else:
                res.append([s, e])
        return res
