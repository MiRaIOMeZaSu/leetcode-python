from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # 动态规划
        last = [1, 1]
        ret = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                ret = max(last[1] + 1, ret)
                last = [last[1] + 1, 1]
            elif arr[i] < arr[i - 1]:
                ret = max(last[0] + 1, ret)
                last = [1, last[0] + 1]
            else:
                last = [1, 1]
        return ret


if __name__ == "__main__":
    Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9])
