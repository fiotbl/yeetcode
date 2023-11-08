class MyQueue:

    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        x = self.queue[0]
        self.queue = self.queue[1:]
        return x
        
    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()