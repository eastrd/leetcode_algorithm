class Solution:
    def repeatedStringMatch(self, A: 'str', B: 'str') -> 'int':
        s = max(int(len(B) / len(A) + 0.9), 1)
        if B in A * s:
            return s
        if B in A * (s+1):
            return s+1
        return -1
