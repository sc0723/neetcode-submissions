class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        temp = ['[', '{', '(']
        openChars = set(temp)

        for c in s:
            if c in openChars:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if c == '}' and top == '{' or c == ']' and top == '[' or c == ')' and top == '(':
                    stack.pop()

                else:
                    return False

        if len(stack) != 0:
            return False
        return True