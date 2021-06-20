class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            ch = num[i]
            n = int(ch)
            if n % 2 != 0:
                return num[:i + 1]
        return ""


if __name__ == "__main__":
    print(Solution().largestOddNumber("35472"))
