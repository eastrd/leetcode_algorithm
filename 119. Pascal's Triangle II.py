class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def generate(row):
            if row == 0:
                return []
            if row == 1:
                return [1]
            if row == 2:
                return [1, 1]
            res = [1]
            prev = generate(row-1)
            for i in range(len(prev) - 1):
                res.append(prev[i] + prev[i+1])
            res.append(1)
            return res
        return generate(rowIndex+1)
