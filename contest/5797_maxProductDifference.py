from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # 找到两个最大值和两个最小值
        size = len(nums)
        lastIndex = 0
        pivot = nums[0]
        for i in range(1, size):
            if nums[i] > pivot:
                pivot = nums[i]
                lastIndex = i
        temp = nums[lastIndex]
        nums[lastIndex] = nums[size - 1]
        nums[size - 1] = temp
        lastIndex = 0
        pivot = nums[0]
        for i in range(1, size - 1):
            if nums[i] > pivot:
                pivot = nums[i]
                lastIndex = i
        temp = nums[lastIndex]
        nums[lastIndex] = nums[size - 2]
        nums[size - 2] = temp
        if size != 4:
            # 寻找最小
            pivot = nums[size - 3]
            lastIndex = size - 3
            for i in range(size - 4, -1, -1):
                if nums[i] < pivot:
                    pivot = nums[i]
                    lastIndex = i
            temp = nums[lastIndex]
            nums[lastIndex] = nums[0]
            nums[0] = temp
            pivot = nums[size - 3]
            lastIndex = size - 3
            for i in range(size - 4, 0, -1):
                if nums[i] < pivot:
                    pivot = nums[i]
                    lastIndex = i
            temp = nums[lastIndex]
            nums[lastIndex] = nums[1]
            nums[1] = temp
        return nums[-1] * nums[-2] - nums[0] * nums[1]


if __name__ == "__main__":
    print(Solution().maxProductDifference([1, 6, 7, 5, 2, 4, 10, 6, 4]))
