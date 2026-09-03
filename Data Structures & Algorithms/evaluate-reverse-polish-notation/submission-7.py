import sys

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}


        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                term1 = stack.pop()
                term2 = stack.pop()
                if tokens[i] == "+":
                    stack.append(term2 + term1)
                elif tokens[i] == "-":
                    stack.append(term2 - term1)
                elif tokens[i] == "*":
                    stack.append(term2 * term1)
                elif tokens[i] == "/":
                    stack.append(int(float(term2) / term1))
            print(stack)       
        return stack[-1]





