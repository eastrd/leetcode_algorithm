class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def robin(txt):
            res = 0
            for c in txt:
                res += ord(c)
            return res
        needle_hash = robin(needle)
        
        if len(needle) > len(haystack):
            return -1
        if not needle:
            return 0
        if len(needle) == len(haystack):
            return 0 if needle == haystack else -1
        
        l = 0
        r = len(needle)
        
        current = robin(haystack[l:r])
        
        while True:
            if current == needle_hash and haystack[l:r] == needle:
                return l
            if r == len(haystack):
                return -1
            current -= robin(haystack[l])
            current += robin(haystack[r])
            l += 1
            r += 1
