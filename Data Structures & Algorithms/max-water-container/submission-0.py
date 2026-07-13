class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                area = max(area, min(heights[i], heights[j]) * (j - i))
        
        return area