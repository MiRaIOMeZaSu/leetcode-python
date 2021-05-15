class Solution:
    def __init__(self) -> None:
        self.table = ["M", "D", "C", "L", "X", "V", "I"]
        self.five = set(["D", "L", "V"])
        self.nums = [1000, 500, 100, 50, 10, 5, 1]
        self.m = {}
        for i in range(len(self.table)):
            self.m[self.table[i]] = i

    def romanToInt(self, s: str) -> int:
        # 读取识别的方向?
        # 从前往后
        index = 0
        ret = 0
        while s and index < len(self.table):
            if len(s) > 1:
                i = self.m[s[1]]
                if i + 1 < len(self.table) and s[0] == self.table[i + 1]:
                    # 此时为4
                    ret += self.nums[i] - self.nums[i + 1]
                    s = s[2:]
                    continue
                elif i + 2 < len(self.table) and s[0] == self.table[i + 2]:
                    # 此时为9
                    ret += self.nums[i] - self.nums[i + 2]
                    s = s[2:]
                    continue
            # 直接往后读即可
            # 此时为1-3或6-8
            if not s:
                break
            if s[0] in self.five:
                # 6-8
                tempIndex = self.m[s[0]]
                ret += self.nums[tempIndex]
                s = s[1:]
                if s:
                    tempIndex += 1
                    while s and s[0] == self.table[tempIndex]:
                        ret += self.nums[tempIndex]
                        s = s[1:]
            else:
                # 1-3
                tempIndex = self.m[s[0]]
                while s and s[0] == self.table[tempIndex]:
                    ret += self.nums[tempIndex]
                    s = s[1:]
        return ret


if __name__ == "__main__":
    ret = Solution().romanToInt("MCMXCIV")
    print(ret)
