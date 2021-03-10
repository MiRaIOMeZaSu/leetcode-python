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

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 先根据end排序
        size = len(points)
        if size == 0:
            return 0
        points = [self.myList(i) for i in points]
        points.sort()
        newList = [points[0]]
        end = points[0][-1]
        i = 1
        while i < size:
            if(points[i][0] > end):
                end = points[i][-1]
                newList.append(points[i])
            i = i + 1
        return len(newList)


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
