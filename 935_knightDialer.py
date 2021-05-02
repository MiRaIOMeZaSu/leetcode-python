class Solution:
    def __init__(self):
        # 使用动态规划,记录每个数字在每个位数情况下的数量,从小到大
        # 0只会导致4和6的下一位不同,其他情况都是对称的
        # 先列出可以跳跃的位置
        # 对称性!
        # 只取1,2,4,5
        self.table = [[4, 4], [2, 4], [1, 1], [], [0, 1, 1], []]
        self.ret = [[1], [1], [1], [], [1], [1]]
        self.nums = [0, 1, 2, 4, 5]

    def knightDialer(self, n: int) -> int:
        for length in range(2, n + 1):
            for num in self.nums:
                temp = 0
                for nextNum in self.table[num]:
                    temp += self.ret[nextNum][length - 2]
                self.ret[num].append(temp)
        ret = 0
        # 1
        ret += 4 * self.ret[1][-1]
        # 0
        ret += self.ret[0][-1]
        # 2
        ret += 2 * self.ret[2][-1]
        # 4
        ret += 2 * self.ret[4][-1]
        if n == 1:
            ret += 1
        return ret % (10 ** 9 + 7)


if __name__ == "__main__":
    Solution().knightDialer(3)
