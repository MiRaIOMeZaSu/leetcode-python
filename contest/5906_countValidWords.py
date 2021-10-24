# class Solution:
#     def countValidWords(self, sentence: str) -> int:
#         ans = 0
#         flag = sentence[0].isalpha()
#         for i in range(1, len(sentence)):
#             if sentence[i] == ' ':
#                 ans += (1 if flag else 0)
#                 flag = False
#             elif not sentence[i].isalpha():
#                 flag = False
#             elif sentence[i - 1] == ' ':
#                 flag = True
#         return ans
import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        strs = sentence.split()
        ans = 0
        for s in strs:
            if re.match("^(([a-z]+\-?[a-z]+)|[a-z]*?)[!.,]?$", s):
                ans += 1
        return ans


if __name__ == "__main__":
    Solution().countValidWords("!this  1-s b8d!")
