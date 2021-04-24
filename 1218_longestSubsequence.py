from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # 重点是保持原有顺序,因此应当在寻找指定值时同时对下标进行验证(哈希表)
        # difference是固定给定的
        # 存储每个数的最长,前面往后取
        dp = {arr[0]: 1}
        ret = 1
        for index in range(1, len(arr)):
            if difference == 0:
                dp.setdefault(arr[index], 0)
            else:
                dp.setdefault(arr[index], 1)
            if arr[index] - difference in dp:
                dp[arr[index]] = max(
                    dp[arr[index]], dp[arr[index] - difference] + 1)
                ret = max(dp[arr[index]], ret)
        return ret


if __name__ == "__main__":
    Solution().longestSubsequence(
        [4, 12, 10, 0, -2, 7, -8, 9, -9, -12, -12, 8, 8], 0)
