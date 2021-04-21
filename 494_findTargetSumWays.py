from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 若使用回溯法,则最大有2**20种可能
        # 不断更新一个dict
        d = {0: 1}
        temp = {}
        for i in nums:
            for key in d.keys():
                for next_key in [key - i, key + i]:
                    if (next_key) not in temp:
                        temp[next_key] = 0
                    temp[next_key] += d[key]
            d = temp
            temp = {}

        return d[target] if target in d else 0
