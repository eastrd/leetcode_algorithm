class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 2:
            return 0
        
        water = 0
        
        for i in range(1, len(height) - 1):
            h = height[i]
            l = i - 1
            r = i + 1
            l_max, r_max = max(height[:i]), max(height[i+1:])

            if l_max > h and r_max > h:
                water += min(l_max, r_max) - h
        
        return water
