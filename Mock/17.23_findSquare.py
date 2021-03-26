from typing import List


class Solution:
    def __init__(self):
        self.r = -1
        self.c = -1
        self.size = 0

    def extend(self, x, y, matrix: List[List[int]]):
        oX = x
        oY = y

        def sub(matrix, oX, x, oY, y):
            while(x > oX):
                flag = 0
                for _x in range(oX, x + 1):
                    if(matrix[_x][y] != 0):
                        flag = 1
                        break
                for _y in range(oY, y + 1):
                    if(matrix[x][_y] != 0):
                        flag = 1
                        break

                if(flag == 0):
                    if(matrix[x][y] == 0):
                        return x - oX + 1
                x -= 1
                y -= 1

            return 1
        while(x < len(matrix) and y < len(matrix)):
            for _x in range(oX, x):
                if(matrix[_x + 1][oY] != 0):
                    return sub(matrix, oX, x - 1, oY, y - 1)
            for _y in range(oY, y + 1):
                if(matrix[oX][_y] != 0):
                    return sub(matrix, oX, x - 1, oY, y - 1)
            x += 1
            y += 1
        return sub(matrix, oX, x - 1, oY, y - 1)

    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        # 使用一个函数每次进行判断
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if(matrix[i][j] == 0):
                    if (min(len(matrix) - i, len(matrix) - j) <= self.size):
                        continue
                    size = self.extend(i, j, matrix)
                    if(size > self.size):
                        self.r = i
                        self.c = j
                        self.size = size
        return [self.r, self.c, self.size] if self.c >= 0 else []


if __name__ == "__main__":
    print(Solution().findSquare(
        [[1, 1, 1, 0, 1, 1, 0, 1, 0, 0],
         [0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
         [0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
         [1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
         [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
         [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
         [1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]))
