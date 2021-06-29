class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 每次更改的是最后一位
        div = 26
        curr = columnNumber - 1
        if curr // div >= 26:
            while curr // div > 26:
                div *= 26
        res = ""
        while curr >= 26:
            index = int(curr // div)
            res += chr(ord('A') + index - 1)
            curr = int(curr % div)
            div /= 26
        res += chr(ord('A') + curr)
        return res


if __name__ == "__main__":
    Solution().convertToTitle(27)
