from typing import List


class Solution:
    class myList(list):
        def __init__(self, pres: list):
            for i in pres:
                self.append(i)

        def __lt__(self, other):
            if(self[-1] < other[-1]):
                return True
            elif(self[-1] == other[-1]):
                return True if self[0] > other[0] else False
            else:
                return False

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 先根据end排序
        size = len(intervals)
        if size == 0:
            return 0
        intervals = [self.myList(i) for i in intervals]
        intervals.sort()
        newList = [intervals[0]]
        end = intervals[0][-1]
        i = 1
        while i < size:
            if(intervals[i][0] >= end):
                end = intervals[i][-1]
                newList.append(intervals[i])
            i = i + 1
        return size - len(newList)


if __name__ == "__main__":
    solution = Solution()
    print(solution.eraseOverlapIntervals([[1, 2], [2, 3]]))
