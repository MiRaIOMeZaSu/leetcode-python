class Solution:
    def trailingZeroes(self, n: int) -> int:
        from math import floor
        i = floor(n / 5)
        ret = 0

        def getFive(num):
            x = 0
            while num != 0 and num % 5 == 0:
                x += 1
                num /= 5
            return x

        for i in range(i * 5, 0, -5):
            ret += getFive(i)
        return ret


if __name__ == "__main__":
    Solution().trailingZeroes(130)
