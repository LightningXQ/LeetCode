class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = list()
        self.del_elms = list()

    def push(self, value: int) -> None:
        self.stack.append(value)
        idx = bisect.bisect_left(self.min_stack, value)
        self.min_stack.insert(idx, value)

    def pop(self) -> None:
        val = self.stack.pop()
        self.min_stack.remove(val)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()