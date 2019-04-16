class Solution:
    def trap(self, height: List[int]) -> int:
        
        def find_right_max(current_i):
            r = current_i
            r_max = height[current_i]
            # Get max right height possible
            i = current_i + 1
            while i < len(height):
                if height[i] >= r_max:
                    r_max = height[i]
                    r = i
                i += 1
            return r, r_max
        
        if len(height) < 2:
            return 0
        
        water = 0
        l_max = height[0]
        
        r, r_max = find_right_max(1)
        for i in range(1, len(height) - 1):
            h = height[i]
            l_max = max(l_max, height[i-1])
            if i > r:
                r, r_max = find_right_max(i)
            
            if l_max > h and r_max > h:
                water += min(l_max, r_max) - h
        
        return water
