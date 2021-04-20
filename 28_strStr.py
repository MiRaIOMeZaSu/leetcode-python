import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = re.search(needle, haystack)
        return res.span()[0] if res is not None else -1


if __name__ == "__main__":
    solution = Solution()
    solution.strStr("aabaa", "ac")
