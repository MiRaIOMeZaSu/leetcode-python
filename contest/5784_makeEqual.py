from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # 单纯地计算字符数量即可
        count = [0 for i in range(26)]
        for word in words:
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1
        size = len(words)
        for i in range(26):
            if count[i] % size != 0:
                return False
        return True


if __name__ == "__main__":
    Solution().makeEqual(["abc", "aabc", "bc"])
