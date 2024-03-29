class MinStack:

    def __init__(self):
        self.stack = []
        self.minValues = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minValues.append(min(val, self.minValues[-1] if self.minValues != [] else val))

    def pop(self) -> None:
        self.stack.pop()
        self.minValues.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValues[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()