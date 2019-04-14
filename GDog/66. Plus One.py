class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits
        digits[-1] += 1
        
        if digits[-1] < 10:
            return digits
        
        digits[-1] = 0
        carry = True
        if len(digits) == 1:
            return [1] + digits
            
        for i in range(len(digits)-2, -1, -1):
            if carry:
                digits[i] += 1
                carry = False
                if digits[i] == 10:
                    digits[i] = 0
                    carry = True
        
        if carry:
            return [1] + digits
        return digits
