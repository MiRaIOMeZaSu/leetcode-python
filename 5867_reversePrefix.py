class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        size = len(word)
        for i in range(size):
            if word[i] == ch:
                index = i
                break
        if index == -1 or size == 1:
            return word

        a = self.getReverse(word[:index + 1])
        b = word[index + 1:]
        return a + b

    def getReverse(self, word: str):
        ret = ''
        for ch in word:
            ret = ch + ret
        return ret


if __name__ == "__main__":
    Solution().reversePrefix(word="abcdefd", ch="d")
