class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.l, self.r = 0, 0
        def rec(left, right):
            if left > -1 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > self.r - self.l + 1:
                    self.l, self.r = left, right
                rec(left - 1, right + 1)
        
        if len(s) in [0, 1]:
            return s
        if s == s[::-1]:
            return s
        
        for i in range(len(s)):
            rec(i, i)
            rec(i, i+1)
            
        return s[self.l : self.r+1]
