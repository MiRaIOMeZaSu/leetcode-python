from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 寻找两头
        size = len(nums)
        if size <= 1:
            return False
        self.k = k
        last = 0
        table = dict()
        for i in range(size - 1, -1, -1):
            num = last + nums[i]
            if nums[i] == 0 and i != 0 and nums[i - 1] == 0:
                return True
            key = num % k
            if key == 0 and i < size - 1:
                return True
            if key not in table:
                table[key] = i
            last = num
        pivot = last % k
        # 开始计算前缀
        last = 0
        curr = last
        for i in range(size):
            curr = last + nums[i]
            temp = curr % k
            if temp == 0 and i > 0:
                return True
            key = pivot - curr % k
            if key < 0:
                key += k
            # 此处会忽略连续的零的情况
            if key in table and table[key] - i > 2:
                return True
            last = curr
        return False


if __name__ == "__main__":
    Solution().checkSubarraySum([23, 6, 9], 6)
