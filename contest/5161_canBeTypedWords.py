class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        table = set()
        for c in brokenLetters:
            table.add(c)
        result = 0
        for s in text.split(" "):
            flag = True
            for c in s:
                if c in table:
                    flag = False
                    break
            if flag:
                result += 1
        return result