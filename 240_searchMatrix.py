from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二维二分法
        # 每次都是在寻找小于中位数的最大值
        self.m = len(matrix)
        self.n = len(matrix[0])
        x = 0
        y = self.m - 1
        while x < self.n and y > -1:
            if matrix[y][x] > target:
                y -= 1
            elif matrix[y][x] < target:
                x += 1
            else:
                return True
        return False


if __name__ == "__main__":
    Solution().searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
        3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target=5)
