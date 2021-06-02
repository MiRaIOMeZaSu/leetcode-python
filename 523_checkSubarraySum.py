from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 二分法?
        # 给出的数必然大于等于零(不存在窗口内更细分的结果?)
        # 减去超越k的部分,转化为移动窗口问题
        # 应该提前寻找连续的零
        size = len(nums)
        if size <= 1:
            return False
        self.k = k
        for i in range(size):
            nums[i] = nums[i] % k
        # # 开始滑动窗口
        # left = 0
        # right = 1
        table = {nums[0]: 1}
        for i in range(1, size):
            if (k - nums[i]) in table and table[(k - nums[i])] > 0:
                return True
            for key in list(table.keys()):
                table[key] -= 1
                if table[key] <= 0:
                    table.pop(key)
                newKey = (key + nums[i]) % k
                if newKey == 0:
                    return True
                if newKey not in table:
                    table[newKey] = 0
                table[newKey] += 1
            if nums[i] not in table:
                table[nums[i]] = 0
            table[nums[i]] += 1
        return False


if __name__ == "__main__":
    Solution().checkSubarraySum([23, 2, 6, 4, 7], 13)
