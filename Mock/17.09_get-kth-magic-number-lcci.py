# 重点是k除3再乘3

from math import pow
# 序列: [0 0 0] [1 0 0] [0 1 0] [0 0 1] [2 0 0] [1 1 0] [1 0 1] [0 2 0] [0 1 1] [0 0 2]


def getRet(nums=[0, 0, 0]):
    return int(pow(3, nums[0]) * pow(5, nums[1]) * pow(7, nums[2]))


class powList(list):
    def __init__(self, pres: list):
        for i in pres:
            self.append(i)
        self.pow = getRet(self)

    def __lt__(self, other):
        return self.pow < other.pow


class Solution:

    def getKthMagicNumber(self, k: int) -> int:
        depth = 1

        if(k == depth):
            return getRet()
        i = 1
        _sum = 1
        dp = [depth]
        while(depth < k):
            _sum += i + 1
            depth = _sum + dp[i - 1]
            dp.append(depth)
            i += 1
        right = i - 1
        pivot = pow(3, right)
        while(pow(7, i) > pivot and i > 1):
            i -= 1
        pivot = pow(7, right)
        while(pow(3, right + 1) < pivot):
            right += 1
        left = i
        pivotNum = dp[left - 1]
        # 此时得到指定的i的值
        results = []
        for res in range(left, right + 1):
            for x in range(res, -1, -1):
                for y in range(res - x, -1, -1):
                    results.append(powList([x, y, res - x - y]))
        results.sort()
        return results[k - pivotNum - 1].pow


if __name__ == "__main__":
    print(Solution().getKthMagicNumber(9))
