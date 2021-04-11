from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.ret = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 中序遍历
        if root:
            self.solve(root)
        return self.ret

    def solve(self, root: TreeNode):
        if root.left:
            self.solve(root.left)
        self.ret.append(root.val)
        if root.right:
            self.solve(root.right)


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
    solution.inorderTraversal(root)
