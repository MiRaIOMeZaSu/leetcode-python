from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # 使用状压
        # 数字为0~len(arr)-1
        self.arr = arr
        return self.solve(0, len(arr) - 1)

    def solve(self, start, end):
        ret = 0
        bit = 0
        for i in range(start, end + 1):
            bit += 1 << self.arr[i]
            if bit == ((1 << (i + 1)) - 1) - ((1 << start) - 1):
                ret += 1
                ret += self.solve(i + 1, end)
                return ret
        return ret


if __name__ == "__main__":
    Solution().maxChunksToSorted([1, 0, 2, 3, 4])
