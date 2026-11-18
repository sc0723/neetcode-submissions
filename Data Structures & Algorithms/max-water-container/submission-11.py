class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxArea = 0
        while i < j:
            maxArea = max(maxArea, (min(heights[i], heights[j]) * (j - i)))
            if heights[j] <= heights[i]:
                j -= 1
            else:
                i += 1
        
        return maxArea