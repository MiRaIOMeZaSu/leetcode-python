from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # 重点是保持原有顺序,因此应当在寻找指定值时同时对下标进行验证(哈希表)
        # difference是固定给定的
        # 存储每个数的最长,前面往后取
        dp = [1]
        ret = 1
        for index in range(1, len(arr)):
            for j in range(index - 1, -1, -1):
                if arr[j] == arr[index] - difference:
                    dp.append(dp[j] + 1)
                    ret = max(dp[j] + 1, ret)
                    break
            if(len(dp) <= index):
                dp.append(1)
        return ret


if __name__ == "__main__":
    Solution().longestSubsequence(
        [6, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5], -2)
