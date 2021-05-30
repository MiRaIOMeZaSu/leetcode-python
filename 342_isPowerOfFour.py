import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        temp = n
        n = int(math.sqrt(n))
        if n * n != temp:
            return False
        return (n & (n - 1)) == 0
