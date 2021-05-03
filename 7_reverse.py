import math


class Solution:
    def reverse(self, x: int) -> int:
        if x == 2147483647 or x == -2147483648:
            return 0
        if x > 1000000000 and (x % 10) > 2:
            return 0
        isNegative = True
        if x > 0:
            isNegative = False
        else:
            x = -x
        ret = 0
        while x > 0:
            bit = x % 10
            if ret != 0 or bit != 0:
                ret = ret * 10 + bit
            x = (x - bit) / 10
            if ret > 214748364 and x > 0:
                return 0
            elif ret == 214748364 and x > 7:
                return 0

        if isNegative:
            ret = -ret
        return math.ceil(ret)


if __name__ == "__main__":
    Solution().reverse(-2147483412)
