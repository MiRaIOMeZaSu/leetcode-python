class Solution:
    def solve(self, s):
        # 使用动态规划,dp表
        dp = []
        # base case
        count = 0
        for i in s:
            if(i == "x"):
                count += 1
        dp.append((0, count))
        maxRet = count
        for i in range(len(s)):
            if(s[i] == "x"):
                dp.append((dp[i][0], dp[i][1] - 1))
            else:
                # 此时为y
                dp.append((dp[i][0] + 1, dp[i][1]))
            maxRet = dp[i + 1][0] + dp[i + 1][1] if dp[i + 1][0] + \
                dp[i + 1][1] < maxRet else maxRet
        return maxRet


if __name__ == "__main__":
    Solution().solve("xyxxxyxyy")
