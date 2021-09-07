class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL = 0
        countR = 0
        charR = 'R'
        result = 0
        for i in range(len(s)):
            if s[i] == charR:
                countR += 1
            else:
                countL += 1
            if countL == countR:
                result += 1
        return result
