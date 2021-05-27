class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        pivot = 1
        maxNum = max(x, y)
        while pivot <= maxNum and pivot < 1073741825:
            flag1 = ((pivot | x) == x)
            flag2 = ((pivot | y) == y)
            if flag2 ^ flag1:
                ret += 1
            pivot = pivot << 1
        return ret


if __name__ == "__main__":
    Solution().hammingDistance(1, 4)
