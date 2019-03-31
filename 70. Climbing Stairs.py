class Solution:
    def climbStairs(self, n: int) -> int:
        self.mem = [None] * (n + 1)
        return self.helper(n)
    
    def helper(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.mem[n]:
            return self.mem[n]
        else:
            self.mem[n] = self.helper(n - 1) + self.helper(n - 2)
            return self.mem[n]
