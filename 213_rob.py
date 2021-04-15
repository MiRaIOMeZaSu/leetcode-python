from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 使用动态规划
        if(len(nums) == 1):
            return nums[0]
        self.numbers = nums
        return max(self.dp(1, len(nums) - 1), self.dp(0, len(nums) - 2))

    def dp(self, left, right):
        dont = 0
        doit = self.numbers[left]
        for i in range(left + 1, right + 1):
            temp = doit
            doit = dont + self.numbers[i]
            dont = max(temp, dont)
        return max(dont, doit)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.rob([2, 1, 2, 6, 1, 8, 10, 10])
    print(ret)
