from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # 顺序一趟倒序一趟计算当前下标到头(结尾)的子数组内实现递减(递增)需要删除的数量
        dp1 = [1]
        dp2 = [1]
        for i in range(1, len(nums)):
            dp1.append(1)
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp1[-1] = max(dp1[j] + 1, dp1[-1])
                elif nums[j] == nums[i]:
                    dp1[-1] = max(dp1[j], dp1[-1])
                    break
            # 另一边
            x = len(nums) - 1 - i
            dp2.insert(0, 1)
            for j in range(x + 1, len(nums)):
                if nums[j] < nums[x]:
                    dp2[0] = max(dp2[-(len(nums) - j)] + 1, dp2[0])
                elif nums[j] == nums[x]:
                    dp2[0] = max(dp2[-(len(nums) - j)], dp2[0])
                    break
        ret = len(nums) - 3
        for i in range(1, len(nums) - 1):
            # 以当前坐标作为山顶
            if dp1[i] == 1 or dp2[i] == 1:
                continue
            length = dp1[i] + dp2[i] - 1
            ret = min(len(nums) - length, ret)
        return ret


if __name__ == "__main__":
    Solution().minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1])
