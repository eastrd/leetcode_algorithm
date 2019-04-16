class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two pointers to iterate from left and right
        if len(s) < 2:
            return True
        
        # Length >= 2
        l, r = 0, len(s) - 1
        while l < r:
            while not (s[l].lower().isalpha() or s[l].lower().isnumeric()) and l < r:
                l += 1
            while not (s[r].lower().isalpha() or s[r].lower().isnumeric()) and l < r:
                r -= 1
            # print(l, r)
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
