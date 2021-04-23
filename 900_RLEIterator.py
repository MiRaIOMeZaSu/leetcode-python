from typing import List


class RLEIterator:

    def __init__(self, A: List[int]):
        self.d = []
        self.arr = []
        self.sum = 0
        for i in range(1, len(A), 2):
            self.arr.append(A[i])
            self.d.append(A[i - 1])
            self.sum += A[i - 1]

    def next(self, n: int) -> int:
        if len(self.arr) <= 0:
            return -1
        if n > self.sum:
            self.d = []
            self.arr = []
            self.sum = 0
            return -1
        if n == self.d[0]:
            self.d.pop(0)
            ret = self.arr[0]
            self.arr.pop(0)
            self.sum -= n
            return ret
        elif n < self.d[0]:
            self.d[0] -= n
            self.sum -= n
            return self.arr[0]
        else:
            n -= self.d[0]
            self.sum -= self.d[0]
            self.d.pop(0)
            self.arr.pop(0)
            return self.next(n)

    # Your RLEIterator object will be instantiated and called as such:
    # obj = RLEIterator(A)
    # param_1 = obj.next(n)


if __name__ == "__main__":
    pass
