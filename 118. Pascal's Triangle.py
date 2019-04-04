class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Number of elements == numRows
        # Sum == 2 ^ (numRows - 1)
        # 
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]
        res = [
            [1],
            [1, 1],
        ]
        
        i = 2
        while i < numRows:
            j = 0
            new_row = [1]
            # Loop through previous array's index
            while j < len(res[i-1]):
                if j == len(res[i-1]) - 1:
                    new_row.append(1)
                else:
                    new_row.append(res[i - 1][j] + res[i - 1][j + 1])
                j += 1
            i += 1
            res.append(new_row)
        return res
