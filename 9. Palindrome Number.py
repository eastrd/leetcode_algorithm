class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[~i]:
                return False
        return True
        
        
     
