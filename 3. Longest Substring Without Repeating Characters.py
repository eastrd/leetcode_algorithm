class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = start = 0
        count = {}
        for idx, c in enumerate(s):
            if c not in count or count[c] < start:
                longest = max(longest, idx - start + 1)
            else:
                start = count[c] + 1
            count[c] = idx
        return longest
