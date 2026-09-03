class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        currMax = 0

        while j > i:
            width = j - i
            height = min(heights[i], heights[j])
            currMax = max(width * height, currMax)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return currMax

