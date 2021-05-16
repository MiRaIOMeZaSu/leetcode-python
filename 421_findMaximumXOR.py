from typing import List


class Solution:
    def __init__(self) -> None:
        temp = 1
        self.table = [temp]
        for i in range(30):
            self.table.append(self.table[-1] * 2)

    def findMaximumXOR(self, nums: List[int]) -> int:
        # 必须保证i<=j
        otherSet = set(nums)
        nums = list(otherSet)
        nums.sort()
        size = len(nums)
        # 通过位移获得相应位数?
        # 为位数建立索引?
        # nums[i]位数为31
        # 保证异或的两个数字一大一小以保证去重
        hasBit = [set() for i in range(32)]
        # 开始初始化
        maxBit = 0
        for i in range(size):
            num = nums[i]
            temp = num
            j = 0
            while j < len(self.table) and num != 0:
                if self.table[j] | temp == temp:
                    hasBit[j + 1].add(i)
                    maxBit = max(j + 1, maxBit)
                    temp ^= self.table[j]
                j += 1
        while len(hasBit[maxBit]) == size:
            maxBit -= 1
        minIndex = size
        for i in hasBit[maxBit]:
            minIndex = min(minIndex, i)
        ret = nums[0] ^ nums[-1]
        # maxBit必为其中之一
        otherSet = {i for i in range(size)}
        otherSet.difference_update(hasBit[maxBit])
        for i in range(size - 1, minIndex - 1, -1):
            num = nums[i]
            lastTempSet = otherSet.copy()
            for bit in range(maxBit - 1, 0, -1):
                if i in hasBit[bit]:
                    # 寻找此为没有的
                    currTempSet = lastTempSet.difference(hasBit[bit])
                else:
                    # 寻找此为有的
                    currTempSet = lastTempSet.intersection(hasBit[bit])
                if not currTempSet:
                    currTempSet = lastTempSet
                else:
                    lastTempSet = currTempSet
                if len(currTempSet) == 1:
                    # 此时为最优解
                    temp = currTempSet.pop()
                    ret = max(ret, nums[temp] ^ num)
                    break
        return ret


if __name__ == "__main__":
    ret = Solution().findMaximumXOR(
        [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70])
    print(ret)
