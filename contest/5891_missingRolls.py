from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        targetTotal = mean * (n + m)
        currTotal = sum(rolls)
        restTotal = targetTotal - currTotal
        ans = []
        if n * 6 < restTotal or n * 1 > restTotal:
            return ans
        avg = restTotal // n
        rest = restTotal - n * avg
        for i in range(n):
            ans.append(avg)
            if rest > 0:
                rest -= 1
                ans[-1] += 1
        return ans
