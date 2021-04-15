from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 使用动态规划
        _max = 0
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
            if(i < len(nums) - 2):
                _max = max(_max, dp[i][0] +
                           (0 if haveFisrt[i][0] else nums[-1]),
                           dp[i][0] +
                           (nums[-1] - nums[0] if haveFisrt[i][0] else nums[-1]))
                _max = max(_max, dp[i][1] +
                           (0 if haveFisrt[i][1] else nums[-1]),
                           dp[i][1] +
                           (nums[-1] - nums[0] if haveFisrt[i][1] else nums[-1]))
        _max = max(_max,
                   dp[-2][1], dp[-2][0] +
                   (nums[-1] if not haveFisrt[i][0] else 0),
                   dp[-2][0] + nums[-1] - (nums[0] if haveFisrt[i][0] else 0))
        return _max


if __name__ == "__main__":
    solution = Solution()
    solution.rob([2, 1, 2, 6, 1, 8, 10, 10])
