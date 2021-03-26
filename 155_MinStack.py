# 使用两个栈
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self._min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(len(self._min) == 0 or self._min[len(self._min) - 1] >= val):
            self._min.append(val)

    def pop(self) -> None:
        if(self.stack[len(self.stack) - 1] == self._min[len(self._min) - 1]):
            self._min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self._min[len(self._min) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    param_4 = obj.getMin()
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
