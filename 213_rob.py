from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 使用动态规划
        if(len(nums) == 1):
            return nums[0]
        dp = []
        haveFisrt = []
        for i in range(len(nums)):
            dp.append([0, 0])
            haveFisrt.append([False, False])
        # dp[0][0] = nums[-1] if len(nums) > 3 else 0
        dp[0][0] = 0
        dp[0][1] = nums[0]
        haveFisrt[0][1] = True
        for i in range(1, len(nums) - 1):
            if(dp[i - 1][1] > dp[i - 1][0]):
                haveFisrt[i][0] = haveFisrt[i - 1][1]
                dp[i][0] = dp[i - 1][1]
            elif(dp[i - 1][1] < dp[i - 1][0]):
                dp[i][0] = dp[i - 1][0]
                haveFisrt[i][0] = haveFisrt[i - 1][0]
            else:
                dp[i][0] = dp[i - 1][0]
                haveFisrt[i][0] = haveFisrt[i - 1][0] and haveFisrt[i - 1][1]
            dp[i][1] = dp[i - 1][0] + nums[i]
            haveFisrt[i][1] = haveFisrt[i - 1][0]
        return max(dp[-2][1], dp[-2][0] + (nums[-1] if not haveFisrt[i][0] else 0), dp[-2][0] + nums[-1] - (nums[0] if haveFisrt[i][0] else 0))


if __name__ == "__main__":
    solution = Solution()
    solution.rob([1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3])
