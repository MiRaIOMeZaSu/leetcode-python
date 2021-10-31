from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lines = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        chMap = {}
        for i in range(len(lines)):
            for ch in lines[i]:
                chMap[ch] = i
        ans = []
        for word in words:
            if len(word) == 1:
                ans.append(word)
                continue
            ch = word[0].lower()
            j = chMap[ch]
            flag = True
            for i in range(1, len(word)):
                if j != chMap[word[i].lower()]:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return ans
