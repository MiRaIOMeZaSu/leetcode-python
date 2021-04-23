from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        visit = set()
        ret = []
        for index in range(len(nums)):
            if nums[index] not in visit:
                visit.add(nums[index])
                temp = [nums[index]]
                for n in range(index + 1, len(nums)):
                    if nums[n] in visit:
                        continue
                    if nums[n] % temp[-1] == 0:
                        temp.append(nums[n])
                        visit.add(nums[n])
                if(len(temp) > len(ret)):
                    ret = temp
        return ret


if __name__ == "__main__":
    pass
