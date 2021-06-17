from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        index = 0
        size = len(nums)
        while(index < size):
            a = nums[index]
            if a == index:
                index += 1
                continue
            b = nums[a]
            if b == a:
                return a
            nums[index] = b
            nums[a] = a
