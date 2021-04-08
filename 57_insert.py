from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 每次插入需要快速寻找后边的值,使用链表?\
        # 要插入的只有一个
        # 先不插入
        if(len(intervals) == 0):
            intervals.append(newInterval)
        head = newInterval[0]
        index = 0
        while(index < len(intervals) and intervals[index][1] < head):
            index += 1
        if(index < len(intervals)):
            if(newInterval[0] <= intervals[index][0]):
                if(newInterval[1] < intervals[index][1]):
                    intervals.insert(index, newInterval)
                else:
                    intervals[index][0] = newInterval[0]
                    if(newInterval[1] > intervals[index][1]):
                        intervals[index][1] = newInterval[1]
            else:
                if(newInterval[1] > intervals[index][1]):
                    intervals[index][1] = newInterval[1]
            pivot = index
            index += 1
            while(index < len(intervals) and intervals[index][0] <= intervals[pivot][1]):
                intervals[pivot][1] = max(
                    intervals[index][1], intervals[pivot][1])
                intervals.remove(intervals[index])
        else:
            intervals.append(newInterval)
        return intervals


solution = Solution()
solution.insert([[1, 5]], [0, 3])
