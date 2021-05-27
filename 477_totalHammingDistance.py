from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # 对于每一位,统计1的数量
        maxNum = max(nums)
        pivot = 1
        ret = 0
        size = len(nums)
        while pivot <= maxNum and pivot < 1073741825:
            count = 0
            for num in nums:
                if num | pivot == num:
                    count += 1
            ret += count * (size - count)
            pivot = pivot << 1
        return ret
