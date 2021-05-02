class Solution:
    def integerBreak(self, n: int) -> int:
        # 动态规划,使用数组表示指定下标为和的最大乘积
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            last = 0
            for j in range(i - 1, 0, -1):
                curr = max(dp[i - j] * j, (i - j) * j)
                if(last > curr):
                    dp.append(last)
                    break
                last = curr
            if(len(dp) != i + 1):
                dp.append(last)
        return dp[n]


if __name__ == "__main__":
    Solution().integerBreak(10)
