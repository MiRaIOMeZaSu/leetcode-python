from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ret = []
        table = [candiesCount[0]]
        for i in range(1, len(candiesCount)):
            table.append(table[-1] + candiesCount[i])
        for query in queries:
            favoriteType = query[0]
            favoriteDay = query[1] + 1
            dailyCap = query[2]
            if favoriteType == 0:
                ret.append(favoriteDay <= table[0])
            elif favoriteDay <= table[favoriteType]:
                if dailyCap * favoriteDay <= table[favoriteType - 1]:
                    ret.append(False)
                else:
                    ret.append(True)
            # elif favoriteDay == table[favoriteType]:
            #     ret.append(True)
            else:
                ret.append(False)
        return ret


if __name__ == "__main__":
    Solution().canEat([16, 38, 8, 41, 30, 31, 14, 45, 3, 2, 24, 23, 38, 30, 31, 17, 35, 4, 9, 42, 28, 18, 37, 18, 14, 46, 11, 13, 19, 3, 5, 39, 24, 48, 20, 29,
                       4, 19, 36, 11, 28, 49, 38, 16, 23, 24, 4, 22, 29, 35, 45, 38, 37, 40, 2, 37, 8, 41, 33, 8, 40, 27, 13, 4, 33, 5, 8, 14, 19, 35, 31, 8, 8], [[43, 1054, 49]])
