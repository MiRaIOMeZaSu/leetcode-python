import re


class Solution:
    def replaceSpace(self, s: str) -> str:
        ret = ""
        size = len(s)
        for index in range(size):
            ch = s[index]
            if ch == " ":
                ret += "%20"
            else:
                ret += ch
            index += 1
        return ret
