class Solution:
    def numDecodings(self, s: str) -> int:
        # 使用动态规划
        size = len(s)
        if size == 1:
            return 1 if s[0] != '0' else 0
        dp = [[0, 0] for i in range(size)]
        if(s[0] == '0'):
            dp[0][0] = 0
            dp[0][1] = 0
            if(s[1] == '0'):
                dp[1][0] = 0
            else:
                dp[1][0] = dp[0][0]
        else:
            dp[0][0] = 1
            if(s[0] < '2' or (s[0] == '2' and s[1] < '7')):
                dp[1][1] = 1
            else:
                dp[1][1] = 0
            dp[1][0] = 1 if s[1] != '0' else 0
        # base case完成开始完善dp表
        for i in range(2, len(s)):
            small = s[i - 1] < '3' and s[i - 1] > '0'
            if(s[i] == '0'):
                dp[i][0] = 0
                if(small):
                    dp[i][1] = dp[i - 2][0] + dp[i - 2][1]
                else:
                    dp[i][1] = 0
            else:
                dp[i][0] = dp[i - 1][1] + dp[i - 1][0]
                if(small and (s[i - 1] < '2' or (s[i - 1] == '2' and s[i] < '7'))):
                    dp[i][1] = dp[i - 2][0] + dp[i - 2][1]
                else:
                    dp[i][1] = 0
        return dp[size - 1][0] + dp[size - 1][1]


if __name__ == "__main__":
    solution = Solution()
    ret = solution.numDecodings("2611055971756562")
    print(ret)
