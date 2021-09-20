from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1,
        }
        ans = 0
        for s in operations:
            ans += d[s]
        return ans
