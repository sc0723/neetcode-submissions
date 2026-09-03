class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []

        pairs = {'}' : '{', ')' : '(', ']' : '['}

        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                    if pairs[c] != top:
                        return False
                else:
                    return False
        
        if stack:
            return False
            
        return True
