import re


class Solution:
    def replaceSpace(self, s: str) -> str:
        return re.sub(" ", "%20", s)
