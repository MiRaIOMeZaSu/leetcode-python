from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        if maxNum % minNum == 0:
            return minNum
        last = 1
        for i in range(1, minNum):
            if minNum % i == 0 and maxNum % i == 0:
                last = i
        return last
