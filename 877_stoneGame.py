class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # 使用二维表格
        dp_table = []
        size = len(piles)
        for i in range(0, size):
            dp_table.append([])
            for j in range(0, size):
                dp_table[i].append([0, 0])
        for i in range(0, size):
            dp_table[i][i] = [piles[i], 0]
        # 初始化完毕
        # 由于特殊的性质而使用特殊的遍历法
        for i in range(size - 2, -1, -1):
            for j in range(i + 1, size):
                # 先手
                left = piles[i]
                right = piles[j]
                first_left = dp_table[i + 1][j][1] + left
                second_right = right + dp_table[i][j - 1][1]
                if (first_left > second_right):
                    # 先手选左边界
                    dp_table[i][j][0] = first_left
                    # 后手
                    # 此时给我留下的是piles区间内去除先手取得部分的新先手
                    dp_table[i][j][1] = dp_table[i + 1][j][0]
                else:
                    # 先手
                    dp_table[i][j][0] = second_right
                    # 后手
                    dp_table[i][j][1] = dp_table[i][j - 1][0]

        return dp_table[0][size - 1][0] > dp_table[0][size - 1][1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.stoneGame([5, 3, 4, 5]))
