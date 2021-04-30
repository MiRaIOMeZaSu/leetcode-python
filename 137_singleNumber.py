from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        times = 1
        last = nums[0]
        for i in range(1, len(nums)):
            if(nums[i] == last):
                times += 1
            elif times == 1:
                return last
            else:
                last = nums[i]
                times = 1
        return last


if __name__ == "__main__":
    Solution().singleNumber([30000, 500, 100, 30000, 100, 30000, 100])
