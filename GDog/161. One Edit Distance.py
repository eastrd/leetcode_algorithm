class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s and not t:
            return False
        diff = abs(len(s) - len(t))
        if diff > 1:
            return False
        # Deal with insert / delete
        if diff == 1:
            if not s or not t:
                return True
            short, long = sorted([s,t], key=lambda x: len(x))
            i = 0
            while i < len(short):
                if short[i] == long[i]:
                    i += 1
                else:
                    return short[i:] == long[i+1:]
            return True
        # Deal with Substitution, diff == 0
        i = 0
        while i < len(s):
            if s[i] == t[i]:
                i += 1
            else:
                return s[i+1:] == t[i+1::]
        return False
