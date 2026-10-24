class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                curr = board[r][c]
                
                if curr == ".":
                    continue
                
                box_val = (r // 3) * 3 + (c // 3)

                if curr in rows[r] or curr in cols[c] or curr in box[box_val]:
                    return False
                
                rows[r].add(curr)
                cols[c].add(curr)
                box[box_val].add(curr)
        
        return True
