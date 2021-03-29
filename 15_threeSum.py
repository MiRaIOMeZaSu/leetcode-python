from typing import List

''' 选择的方法
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
        for i in range(0, len(nums)):
            for n in range(i + 1, len(nums)):
                temp = [nums[i], nums[n]]
                _sum = nums[i] + nums[n]
                if(0 - _sum in table and table[0 - _sum][len(table[0 - _sum]) - 1] > n):
                    temp.append(0 - _sum)
                    ret.append(temp)
        return ret
'''


class threeNum(list):
    def __init__(self):
        self.d = {}

    def __eq__(self, o):
        for i in self.d.keys():
            if not (i in o.d and self.d[i] == o.d[i]):
                return False
        return True

    def extend(self, iterable):
        super(threeNum, self).extend(iterable)
        for i in iterable:
            self.d[i] = self.d[i] + 1 if i in self.d else 1


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
        for i in range(0, len(nums)):
            for n in range(i + 1, len(nums)):
                _sum = nums[i] + nums[n]
                if(0 - _sum in table and table[0 - _sum][len(table[0 - _sum]) - 1] > n):
                    temp = threeNum()
                    temp.extend([nums[i], nums[n], 0 - _sum])
                    if temp not in ret:
                        ret.append(temp)
        return ret


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
