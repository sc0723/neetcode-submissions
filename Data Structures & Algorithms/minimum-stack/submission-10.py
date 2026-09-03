class MinStack:

    def __init__(self):
        self.stack = []
        self.currentMin = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.currentMin:
            self.currentMin.append(val)
        else:
            self.currentMin.append(min(val, self.currentMin[-1]))
    def pop(self) -> None:
        self.stack.pop()
        self.currentMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currentMin[-1]
        
