from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 动态规划?
        # 先排序,再依次左右寻找?
        # 任意区间的最小值
        # 移动窗口+小顶堆(延迟删除)(暴力法))
        # 单调栈法,寻找左右两边第一个比当前位置低的位置
        size = len(heights)
        dp1 = [1 for i in range(size)]
        dp2 = [1 for i in range(size)]
        stack = [0]
        for i in range(1, size):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # 此时获得长度
            dp1[i] = i - stack[-1] if len(stack) > 0 else i + 1
            # 此处应该还有添加操作!
            stack.append(i)
        stack = [size - 1]
        for i in range(size - 2, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            dp2[i] = stack[-1] - i if len(stack) > 0 else size - i
            stack.append(i)
        # 此时开始进行遍历计算
        ret = 0
        for i in range(0, size):
            ret = max(ret, heights[i] * (dp1[i] + dp2[i] - 1))
        return ret
        # ! 可以优化的点: 1. 创建数组的方式[1] * size
        # ! 2. 判断空的方式: if []
        # ! 3. 最大值的判断方法:


if __name__ == "__main__":
    Solution().largestRectangleArea([2, 4])
