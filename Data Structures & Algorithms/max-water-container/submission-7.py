class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        max_area = 0

        while i < j:
            max_area = max(max_area, (j-i) * min(heights[i], heights[j]))

            if heights[j] <= heights[i]:
                j -= 1
            else:
                i += 1
        
        return max_area
    