from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 任选两个,寻找和为零
        table = {}
        for i in range(0, len(nums)):
            if nums[i] not in table:
                table[nums[i]] = [i]
            else:
                table[nums[i]].append(i)
        ret = []
        alreadyIn = set()
        for i in range(0, len(nums)):
            for n in range(i + 1, len(nums)):
                _sum = nums[i] + nums[n]
                if(0 - _sum in table and table[0 - _sum][len(table[0 - _sum]) - 1] > n):
                    temp = [nums[i], nums[n], 0 - _sum]
                    temp.sort()
                    s = str(temp[0]) + str(temp[1])
                    if s not in alreadyIn:
                        ret.append(temp)
                        alreadyIn.add(s)
        return ret


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4, 1, 2, 4, 6, 4, 0, 2]))
