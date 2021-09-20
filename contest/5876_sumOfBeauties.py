from typing import List
import random


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        # 使用存储最大最小值的方法
        size = len(nums)
        left_max = [nums[0]]
        right_min = [float('inf') for i in range(size - 1)]
        right_min.append(nums[-1])
        for i in range(1, size):
            if nums[i] > left_max[-1]:
                left_max.append(nums[i])
            else:
                left_max.append(left_max[-1])
        for i in range(size - 2, -1, -1):
            if nums[i] >= right_min[i + 1]:
                right_min[i] = right_min[i + 1]
            else:
                right_min[i] = nums[i]
        ans = 0
        for i in range(1, size - 1):
            if nums[i] > left_max[i - 1] and nums[i] < right_min[i + 1]:
                ans += 2
            elif nums[i] > nums[i - 1] and nums[i] < nums[i + 1]:
                ans += 1
        return ans


if __name__ == "__main__":
    # print(Solution().sumOfBeauties([1]))
    solution = Solution()
    for i in range(100):
        arr = []
        size = random.randint(3, 10000)
        for j in range(size):
            arr.append(random.randint(1, 100000))
        print(solution.sumOfBeauties(arr))
