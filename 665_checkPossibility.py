from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 如果存在多个则不满足
        # 发现一个不满足情况则,跳过,再次发现时结束判断
        canChange = True
        lastNum = nums[0]
        if(len(nums) > 1):
            nextMin = min(nums[1], nums[0])
        else:
            return True
        for index in range(1, len(nums)):
            if(lastNum > nums[index]):
                if(canChange):
                    if index == len(nums) - 1:
                        return True
                    else:
                        if nums[index + 1] < nums[index - 1] and nextMin > nums[index]:
                            return False
                    canChange = not canChange
                else:
                    return False
            nextMin = min(nums[index], lastNum)
            lastNum = nums[index]
        return True


if __name__ == "__main__":
    Solution().checkPossibility([3, 4, 2, 3])
