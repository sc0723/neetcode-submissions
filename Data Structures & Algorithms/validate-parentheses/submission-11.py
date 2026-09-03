class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []

        pairs = {'}': '{', ']' : '[', ')':'('}

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                    print('Top: ', top)
                    if pairs[c] != top:
                        return False
                else:
                    return False
            print(stack)
        if stack:
            return False
        
        return True
