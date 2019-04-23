class Solution:
    def climbStairs(self, n: int) -> int:
        self.mem = {}
        def recur(n):
            if n in self.mem:
                return self.mem[n]
            if n in [0, 1, 2, 3]:
                return n
            res = recur(n-1) + recur(n-2)
            self.mem[n] = res
            return res
        return recur(n)
