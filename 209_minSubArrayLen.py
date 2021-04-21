from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 双指针
        total = 0
        left = 0
        right = 0
        ret = float('inf')
        while(right < len(nums)):
            while(total < target and right < len(nums)):
                total += nums[right]
                right += 1
            if(right == len(nums) and left == 0):
                if(total < target):
                    return 0
            ret = min(ret, right - left)
            while(total >= target):
                total -= nums[left]
                left += 1
            ret = min(ret, right - left + 1)
        return ret


if __name__ == "__main__":
    Solution().minSubArrayLen(
        213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12])
