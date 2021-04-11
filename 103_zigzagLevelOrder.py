from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        rets = []
        if(root is None):
            return rets
        ret = []
        base = []
        temp = []
        base.append(root)
        order = True
        start = 0
        end = len(base)
        step = 1
        while len(base) != 0:
            if order:
                start = 0
                end = len(base)
                step = 1
            else:
                start = len(base) - 1
                end = -1
                step = -1
            for i in range(start, end, step):
                node = base[i]
                ret.append(node.val)
                if order:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                else:
                    if node.right:
                        temp.insert(0, node.right)
                    if node.left:
                        temp.insert(0, node.left)
            rets.append(ret)
            ret = []
            base = temp
            temp = []
            order = not order
        return rets


if __name__ == "__main__":
    root = TreeNode(3)
    _2 = TreeNode(9)
    _3 = TreeNode(20)
    root.left = _2
    root.right = _3
    _4 = TreeNode(15)
    _5 = TreeNode(7)
    _3.left = _4
    _3.right = _5
    solution = Solution()
    solution.zigzagLevelOrder(root)
