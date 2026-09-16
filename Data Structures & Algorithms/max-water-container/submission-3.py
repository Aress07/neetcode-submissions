class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l, r = 0, len(heights) - 1
        while l < r:
            surface = min(heights[l], heights[r]) * (r - l)
            maxA = max(maxA, surface)
            if heights[l] > heights[r]: r -=1
            else: l += 1
        return maxA