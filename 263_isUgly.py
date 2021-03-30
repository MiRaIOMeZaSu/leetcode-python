class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        # 重点: 递增增加除取因子的次数
        # 2, 3, 5
        for i in [2, 3, 5]:
            dividend = i
            time = 1
            while(n % dividend == 0):
                n /= dividend
                dividend **= 2
                time *= 2
            dividend /= i
            for x in range(time - 1, 0, -1):
                if(n % dividend == 0):
                    n /= dividend
                    break
                dividend /= i
        return True if n == 1 else False


if __name__ == "__main__":
    print(Solution().isUgly(1800000000))
