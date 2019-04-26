class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        if len(height) == 2:
            return min(height)
        
        i, j = 0, len(height) - 1
        taller = max(i, j)
        max_area = height[i]
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > max_area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return max_area
