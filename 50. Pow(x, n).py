class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.mem = {0: 1, 1: x, 2: x ** 2, 3: x ** 3}
        def pow(n):
            if n in self.mem:
                return self.mem[n]
            elif n % 2 == 0:
                res = pow(n//2) ** 2
                self.mem[n] = res
                return res
            elif n % 3 == 0:
                res = pow(n//3) ** 3
                self.mem[n] = res
                return res
            else:
                res = x ** n
                self.mem[n] = res
                return res
        return pow(n)
