from functools import lru_cache
from typing import List, Tuple


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # 使用记忆法
        self.ans = 0
        self.words = words
        self.score = score
        self.count = [0 for i in range(26)]
        for letter in letters:
            self.count[ord(letter) - ord('a')] += 1
        self.solve(tuple((0 for i in range(26))), 0, 0)
        return self.ans

    @lru_cache(None)
    def solve(self, curr: Tuple[int], index: int, currPoint: int):
        if index >= len(self.words):
            return
        copy = [curr[index] for index in range(26)]
        flag = True
        nextPoint = currPoint
        for i in range(len(self.words[index])):
            ch = ord(self.words[index][i]) - ord('a')
            copy[ch] += 1
            if copy[ch] > self.count[ch]:
                flag = False
                break
            nextPoint += self.score[ch]
        if flag:
            self.solve(tuple(copy), index + 1, nextPoint)
            self.ans = max(nextPoint, self.ans)
        self.solve(curr, index + 1, currPoint)


if __name__ == "__main__":
    Solution().maxScoreWords(words=["dog", "cat", "dad", "good"], letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"], score=[
        1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
