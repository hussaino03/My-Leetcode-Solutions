class MyStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1 is None:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2 is None:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()