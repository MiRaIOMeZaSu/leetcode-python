class Solution:
    def __init__(self) -> None:
        self.nums = [1000, 100, 10, 1]
        self.table = {
            1000: ["M", 100],
            500: ["D", 100],
            100: ["C", 10],
            50: ["L", 10],
            10: ["X", 1],
            5: ["V", 1],
            1: ["I", 0]
        }

    def handle(self, size, times):
        item = self.table[size]
        ret = item[0]
        if times <= 3:
            return ret * times
        elif times == 4 or times == 9:
            return self.table[item[1]][0] + ret
        ret += self.table[item[1]][0] * (times - 5)
        return ret

    def intToRoman(self, num: int) -> str:
        # 最多4位
        ret = ""
        i = 0
        while num > 0:
            pivot = num // self.nums[i]
            if pivot > 0:
                size = self.nums[i]
                if pivot == 9:
                    size = 10 * size
                elif pivot >= 4:
                    size = 5 * size
                ret += self.handle(size, pivot)
                num = num % self.nums[i]
            i += 1
        return ret


if __name__ == "__main__":
    ret = Solution().intToRoman(58)
    print(ret)
