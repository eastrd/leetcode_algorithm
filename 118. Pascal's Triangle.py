class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.res = []
        def recur(row):
            if row == 0:
                return []
            if row == 1:
                self.res.append([1])
                return [1]
            if row == 2:
                self.res.append([1]) 
                self.res.append([1, 1])
                return [1, 1]
            res = [1]
            prev_row = recur(row-1)
            for i in range(len(prev_row)-1):
                res.append(prev_row[i] + prev_row[i+1])
            res.append(1)
            self.res.append(res)
            return res
        recur(numRows)
        return self.res
