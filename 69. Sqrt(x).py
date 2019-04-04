class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        if x in [1,2]:
            return 1
        left = 1
        right = (x + 1) // 2
        while left <= right:
            mid = (left + right) // 2
            # print(left, mid, right)
            if mid * mid <= x and (mid + 1) ** 2 > x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return mid
