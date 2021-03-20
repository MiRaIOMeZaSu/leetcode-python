from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originColor = image[sr][sc]
        if(newColor == originColor):
            return image
        self.fill(image, sr, sc, newColor, originColor)
        return image

    def fill(self, image: List[List[int]], sr: int, sc: int, newColor: int, originColor: int):
        if(not self.inArea(image, sr, sc, originColor)):
            return
        image[sr][sc] = newColor
        self.fill(image, sr - 1, sc, newColor, originColor)
        self.fill(image, sr + 1, sc, newColor, originColor)
        self.fill(image, sr, sc - 1, newColor, originColor)
        self.fill(image, sr, sc + 1, newColor, originColor)

    def inArea(self, image, sr, sc, originColor):
        if(sr >= len(image) or sr < 0):
            return False
        if(sc >= len(image[0]) or sc < 0):
            return False
        if(image[sr][sc] != originColor):
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    result = solution.floodFill(image=[[0, 0, 0], [0, 1, 1]],
                                sr=1, sc=1, newColor=1)
    print(result)
