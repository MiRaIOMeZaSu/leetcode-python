from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arr = []
        table = dict()
        for num in nums:
            if num not in table:
                table[num] = 0
                arr.append(num)
            table[num] += num
        arr.sort()
        # 此时开始动态规划
        # dp[i][0]或dp[i][1],dp[i][2]:0表示主动删除,1表示被动删除,2表示跳过
        dp = []
        # 从前往后走的
        dp.append([table[arr[0]], 0, 0])
        ret = table[arr[0]]
        for i in range(1, len(arr)):
            dp.append([0, 0, 0])
            if arr[i - 1] == arr[i] - 1:
                dp[i][0] = table[arr[i]] + max(dp[i - 1][1], dp[i - 1][2])
                dp[i][1] = dp[i - 1][0]
            else:
                greater = max(dp[i - 1][0], dp[i - 1][1])
                dp[i][0] = table[arr[i]] + greater
                dp[i][1] = greater
            dp[i][2] = max(dp[i - 1])
            ret = max(ret, dp[i][0], dp[i][1], dp[i][2])
        return ret


if __name__ == "__main__":
    Solution().deleteAndEarn(
        [45, 44, 47, 46, 44, 44])
