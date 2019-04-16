class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return k
        if len(s) < 2:
            return len(s)
        maximum = 0
        
        l = 0
        r = 0
        index_dict = {}
        while r < len(s):
            # Update index dict with the current char's index
            index_dict[s[r]] = r 
            
            if len(index_dict) > k:
                # Find the char that has the smallest index
                minimum = float("inf")
                char = None
                for c in index_dict:
                    if index_dict[c] < minimum:
                        minimum, char = index_dict[c], c
                        # print("Set minimum to", minimum, char, index_dict[c])
                            
                # Remove the earliest indexed character from dictionary
                del index_dict[char]
                
                # Shift l to closest next position
                l = minimum + 1
                
            else:
                # Update maximum length
                maximum = max(maximum, r - l + 1)
            r += 1
        
        return maximum
