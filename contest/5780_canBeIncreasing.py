from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        size = len(nums)
        flag = False
        i = 1
        while i < size:
            if(nums[i] <= nums[i - 1]):
                if flag:
                    return False
                flag = True
                if i == 1:
                    pass
                elif nums[i] > nums[i - 2]:
                    pass
                elif i != size - 1 and nums[i + 1] <= nums[i - 1]:
                    return False
            i += 1
        return True


if __name__ == "__main__":
    print(Solution().canBeIncreasing([1, 2, 10, 5, 7]))
