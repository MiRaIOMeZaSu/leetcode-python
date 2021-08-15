from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        self.nums = nums
        size = len(nums)
        curr = 1
        nums.sort()
        while curr < size - 1:
            if curr < 1:
                curr = 1
            if nums[curr] + nums[curr] == nums[curr - 1] + nums[curr + 1]:
                # 开始进行替换
                temp = nums[curr + 1]
                nums[curr + 1] = nums[curr]
                nums[curr] = temp
                curr -= 2
            curr += 1
        return nums


if __name__ == "__main__":
    print(Solution().rearrangeArray([1, 5, 2, 6, 3, 7, 4, 8]))
