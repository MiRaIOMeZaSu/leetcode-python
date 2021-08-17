import re


class Solution:
    def checkRecord(self, s: str) -> bool:
        return re.search("LLL", s) is None and re.search("A.*?A", s) is None
