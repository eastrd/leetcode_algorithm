class Solution:
    def fib(self, N: int) -> int:
        self.mem = {0: 0, 1:1}
        def rec(N):
            if N in self.mem:
                return self.mem[N]
            
            if N-1 in self.mem:
                a = self.mem[N - 1]
            else:
                a = rec(N - 1)
                self.mem[N-1] = a
            if N-2 in self.mem:
                b = self.mem[N - 2]
            else:
                b = rec(N - 2)
                self.mem[N-2] = b
            self.mem[N] = a + b
            return a + b
        return rec(N)
