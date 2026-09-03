class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []
        for c in tokens:
            if c not in ops:
                stack.append(int(c))
            else:
                term1 = stack.pop()
                term2 = stack.pop()
                res = 0
                if c == "+":
                    res = term1 + term2
                elif c == "-":
                    res = term2 - term1
                elif c == "*":
                    res = term1 * term2
                else:
                    res = int(term2 / term1)
                stack.append(res)
        
        return stack[-1]