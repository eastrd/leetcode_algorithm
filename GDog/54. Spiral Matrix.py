class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.res = []
        if not matrix or not matrix[0]:
            return self.res
        target = len(matrix) * len(matrix[0])
        
        def helper(m):
            # print(m[0], self.res)
            self.res.extend(m[0])
            if len(m) > 1:
                # Add last element of each row
                for i in range(1, len(m)):
                    self.res.append(m[i][-1])
                if len(m[0]) > 1:
                    # Add last row elements backwards
                    self.res.extend(m[-1][-2::-1])
                    # Add first element back to first row
                    for i in range(len(m)-2, 0, -1):
                        self.res.append(m[i][0])
            if len(self.res) < target:
                m = [row[1:-1] for row in m[1:-1]]
                helper(m)
        
        helper(matrix)
        
        return self.res
