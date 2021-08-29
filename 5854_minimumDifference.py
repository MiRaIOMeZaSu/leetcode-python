from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        k -= 1
        nums.sort()
        ret = float('inf')
        for i in range(len(nums) - k):
            ret = min(nums[i + k] - nums[i], ret)
        return ret
