from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # 通过链表
        nums.sort()
        d_next = {}
        d_count = {}
        count_max = 0
        node_max = nums[0]
        ret = []
        for index in range(len(nums) - 1, -1, -1):
            d_count.setdefault(nums[index], 0)
            d_count[nums[index]] = max(d_count[nums[index]], 0)
            for n in range(index - 1, -1, -1):
                if(nums[index] % nums[n] == 0):
                    d_count.setdefault(nums[n], 0)
                    if(d_count[nums[index]] + 1 >= d_count[nums[n]]):
                        d_next[nums[n]] = nums[index]
                        d_count[nums[n]] = d_count[nums[index]] + 1
                        if(d_count[nums[n]] > count_max):
                            node_max = nums[n]
                            count_max = d_count[nums[n]]
        curr = node_max
        ret.append(curr)
        while curr in d_next:
            ret.append(d_next[curr])
            curr = d_next[curr]
        return ret


if __name__ == "__main__":
    Solution().largestDivisibleSubset([1, 2, 3])
