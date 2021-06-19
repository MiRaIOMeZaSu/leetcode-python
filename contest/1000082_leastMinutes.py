class Solution:
    def leastMinutes(self, n: int) -> int:
        # 二分法?
        # 一共n个插件!
        if n < 3:
            return n
        left = 0
        right = n
        ret = n
        while left < right:
            mid = (left + right) >> 1
            a = self.solve(mid - 1, n)
            b = self.solve(mid, n)
            c = self.solve(mid + 1, n)
            ret = min([ret, a, b, c])
            if a > b:
                left = mid + 1
            elif c > b:
                right = mid - 1
            else:
                return ret
        return ret

    def solve(self, times, n):
        if times == 0:
            return n
        speed = 1
        for i in range(times):
            speed = speed * 2
        temp = 0 if n % speed == 0 else 1
        return times + n // speed + temp


if __name__ == "__main__":
    Solution().leastMinutes(4)
