from typing import List


class Solution:
    def __init__(self) -> None:
        self.m_num = {}
        self.m_count = {}

    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        size = len(rectangles)
        for i in range(size):
            key = rectangles[i][0] / rectangles[i][1]
            if key in self.m_num:
                arr = self.m_num[key]
                for j in range(len(arr)):
                    if arr[j][0] * rectangles[i][1] == arr[j][1] * rectangles[i][0]:
                        self.m_count[key][j] += 1
                        break
                    else:
                        self.m_num[key].append(rectangles[i])
                        self.m_count[key].append(1)
            else:
                self.m_num[key] = [rectangles[i]]
                self.m_count[key] = [1]
        result = 0
        for key in self.m_count.keys():
            arr = self.m_count[key]
            for i in arr:
                result += self.getPairCount(i)
        return result

    def getPairCount(self, num):
        return (((num - 1) * num) >> 1)


if __name__ == "__main__":
    print(Solution().interchangeableRectangles(
        [[4, 8], [3, 6], [10, 20], [15, 30]]))
