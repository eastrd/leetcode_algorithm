class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        i = 0
        target = strs.pop()
        while i < len(target):
            for s in strs:
                if i == len(s) or s[i] != target[i]:
                    return common
            common += target[i]
            i += 1
        return common
