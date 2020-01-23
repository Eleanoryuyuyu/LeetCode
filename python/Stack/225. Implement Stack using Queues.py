class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue = [x] + self.queue
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        x = self.queue[0]
        self.queue.pop(0)
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
print(param_4)