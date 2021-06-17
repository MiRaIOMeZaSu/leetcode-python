from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 先寻找最大值
        size = len(nums)
        maxIndex = -1
        maxNum = size - 1
        for index in range(size):
            if nums[index] == size:
                maxIndex = index
                maxNum = size
                break
        # 位移交换!
        if maxNum != size:
            return size
        index = 0
        while(index < size):
            a = nums[index]
            if index == a:
                index += 1
                continue
            if a == size:
                maxIndex = index
                index += 1
                continue
            b = nums[a]
            nums[a] = a
            nums[index] = b
        return maxIndex


if __name__ == "__main__":
    Solution().missingNumber([1, 2])
