class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        # Binary search for row
        top, bottom = 0, len(matrix) - 1
        
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not (top <= bottom):
            return False
        
        i, j = 0, len(matrix[row]) - 1

        while i <= j:
            mid = (j + i) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        
        return False

        