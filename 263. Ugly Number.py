class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        while num > 1:
            before = num
            if num % 2 == 0:
                num //= 2
            if num % 3 == 0:
                num //= 3
            if num % 5 == 0:
                num //= 5
            if num == before:
                return False
        return True
