class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.mem = []
        for i in range(m + 2):
            self.mem.append([None] * (n + 2))
        self.mem[1][1] = self.mem[1][2] = self.mem[2][1] = 1
        return self.helper(m, n)


    def helper(self, m, n):
        if m < 1 or n < 1:
            return 0
        if self.mem[m][n]:
            return self.mem[m][n]
        self.mem[m][n] = self.helper(m-1, n) + self.helper(m, n-1)
        return self.mem[m][n]
