class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check_match(src, dst):
            if len(src) != len(dst):
                return False
            mapper = {}
            for i in range(len(src)):
                x, y = src[i], dst[i].upper()
                if (x in mapper and mapper[x] != y) or (y in mapper and mapper[y] != x):
                        return False
                mapper[x] = y
                mapper[y] = x
            return True
            
            
        return [w for w in words if check_match(w, pattern)]
