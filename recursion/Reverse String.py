class Solution:
    def reverseString(self, s: List[str], i = None) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Swap elements on both sides
        # Base Case: stop if reaches middle
        if len(s) < 2:
            return
        
        mid = len(s) // 2
        if not i:
            i = 0
        
        # Odd number: don't swap middle one
        if i == mid:
            return s
    
        s[i], s[~i] = s[~i], s[i]
        
        self.reverseString(s, i+1)
