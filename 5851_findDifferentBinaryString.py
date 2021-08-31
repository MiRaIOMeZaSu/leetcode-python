from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # 长度为n
        # 使用深度优先遍历法
        self.nums = nums
        self.s = set()
        self.temp = ['0', '1']
        for string in nums:
            self.s.add(string)
        return self.solve([], 0)

    def solve(self, curr: List[str], index):
        if index >= len(self.nums):
            return self.toString(curr)
        for i in self.temp:
            curr.append(i)
            a = self.solve(curr, index + 1)
            curr.pop()
            if a is not None and a not in self.s:
                return a

    def toString(self, curr):
        ret = ""
        for c in curr:
            ret += c
        return ret


if __name__ == "__main__":
    print(Solution().findDifferentBinaryString(["00", "01"]))
