class MaxQueue:
    def __init__(self):
        self.queue = []
        self.max_queue = []
    def max_value(self) -> int:
        if len(self.queue) == 0:
            return -1
        else:
            return self.max_queue[-1]
    def push_back(self, value: int) -> None:
        self.queue.append(value)
        self.max_queue.append(value)
        i = len(self.max_queue)-2
        j = len(self.max_queue)-1
        while i >=0 and value < self.max_queue[i]:
            self.max_queue[j] = self.max_queue[j-1]
            i -= 1
            j -= 1
        self.max_queue[i+1] = value

    def pop_front(self) -> int:
        if len(self.queue) == 0:
            return -1
        x = self.queue.pop(0)
        self.max_queue.remove(x)
        return x



Q = MaxQueue()
# Q.push_back(1)
# Q.push_back(2)
# print(Q.max_value())
print(Q.pop_front())
print(Q.max_value())
