from typing import List
import re


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0
        for p in patterns:
            if re.search(p, word):
                result += 1
        return result
