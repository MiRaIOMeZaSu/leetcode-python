from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # 动态规划? + 哈希表
        # 严格递增,不存在重复
        self.max = 0
        self.size = len(arr)
        self.table = set()
        for i in range(self.size):
            self.table.add(arr[i])
        self.visit = set()
        left = 0
        while left < self.size - self.max:
            # for left in range(self.size):
            right = left + 1
            while right - 1 < self.size - self.max and right < self.size:
                # for right in range(left + 1, self.size):
                _sum = arr[left] + arr[right]
                # 实际上,每次只要存储这次的结果和上次的结果即可
                if(_sum > arr[-1]):
                    break
                if(_sum in self.table):
                    self.visit.add(self.toString(arr[left], arr[right]))
                    self.max = max(self.max, 3)
                    self.solve(arr[right], _sum, 3)
                right += 1
            left += 1
        return self.max if self.max >= 3 else 0

    def solve(self, left, right, count):
        s = self.toString(left, right)
        if(s not in self.visit):
            _sum = left + right
            if(_sum in self.table):
                self.max = max(self.max, count + 1)
                self.solve(right, _sum, count + 1)

    def toString(self, left, right):
        return str(left) + "," + str(right)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.lenLongestFibSubseq([1, 2, 4])
    print(ret)
