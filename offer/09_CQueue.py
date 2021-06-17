class CQueue:

    def __init__(self):
        self.stackHead = []
        self.stackTail = []

    def appendTail(self, value: int) -> None:
        self.stackTail.append(value)

    def deleteHead(self) -> int:
        if len(self.stackHead) != 0:
            return self.stackHead.pop()
        while len(self.stackTail) != 0:
            # 全部移到stackHead里去
            self.stackHead.append(self.stackTail.pop())
        if len(self.stackHead) != 0:
            return self.stackHead.pop()
        else:
            return -1


if __name__ == "__main__":
    pass
    # Your CQueue object will be instantiated and called as such:
    # obj = CQueue()
    # obj.appendTail(value)
    # param_2 = obj.deleteHead()
