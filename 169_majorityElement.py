from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from math import ceil
        # 寻找出现次数最多的元素
        nums.sort()
        element = nums[0]
        count = 1
        pre = nums[0]
        for i in range(1, len(nums)):
            if(pre == nums[i]):
                count += 1
            else:
                if count >= ceil(len(nums) / 2):
                    return pre
                pre = nums[i]
                count = 1
        return pre if count >= ceil(len(nums) / 2) else element


if __name__ == "__main__":
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
