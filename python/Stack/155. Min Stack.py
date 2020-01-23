class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            min_num = min(self.stack)
        return min_num


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-3)
obj.push(0)
obj.push(-2)
obj.push(-1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
