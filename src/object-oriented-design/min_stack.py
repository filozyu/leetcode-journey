class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            _, min_val = self.stack[-1]
            self.stack.append((x, min(min_val, x)))

    def pop(self) -> None:
        x, _ = self.stack.pop()
        return x

    def top(self) -> int:
        x, _ = self.stack[-1]
        return x

    def getMin(self) -> int:
        _, min_val = self.stack[-1]
        return min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
