from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        self.k = k
        priTable = [nums[0]]
        for i in range(1, len(nums)):
            priTable.append(priTable[-1] + nums[i])
            if self.check(priTable[-1]):
                return True
        for i in range(2, len(nums)):
            # i 为子数组长度
            j = 1
            while j + i - 1 < len(nums):
                if self.check(priTable[j + i - 1] - priTable[j - 1]):
                    return True
                j += 1
        return False

    def check(self, num):
        return (num % self.k) == 0
