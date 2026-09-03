class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding = {'}': '{', ']': '[', ')': '('}

        for c in s:
            if c in corresponding:
                if stack:
                    top = stack.pop()
                    if top != corresponding[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack