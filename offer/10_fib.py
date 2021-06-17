class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        lastlast = 0
        last = 1
        index = 2
        while index <= n:
            nextNum = (last + lastlast) % 1000000007
            lastlast = last
            last = nextNum
            index += 1
        return last
