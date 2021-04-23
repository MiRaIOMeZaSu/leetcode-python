import re


class Solution:

    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 主体是kmp算法
        a_size = len(a)
        b_size = len(b)
        count = b_size // a_size
        string = a * count
        for i in range(count, count + 3):
            if re.search(b, string):
                return i
            string += a
        return -1
