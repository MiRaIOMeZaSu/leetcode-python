from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 简单滑动窗口?
        # 前缀和后缀的决定性
        # 零和一的总数量会由下标展示
        # 先为后缀构件哈希表
        # 以1的数量为标尺
        reverseTre = dict()
        size = len(nums)
        last = 0
        i = size - 1
        ret = 0
        while i > -1:
            if nums[i] == 1:
                last += 1
            else:
                last -= 1
            if last not in reverseTre:
                reverseTre[last] = i
            if last == 0:
                ret = size - i
            i -= 1
        if ret == size:
            return ret
        pivot = last
        last = 0
        for i in range(size):
            if nums[i] == 1:
                last += 1
            else:
                last -= 1
            if last == 0:
                ret = max(ret, i + 1)
            key = pivot - last
            if key in reverseTre and i + 1 < reverseTre[key]:
                ret = max(ret, reverseTre[key] - i - 1)
        return ret


if __name__ == "__main__":
    Solution().findMaxLength([0, 1, 0])
