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
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        list1 = []
        self.solve(root1, list1)
        list2 = []
        self.solve(root2, list2)
        if len(list1) != len(list2):
            return False
        else:
            for i in range(len(list1)):
                if list1[i] != list2[i]:
                    return False
        return True

    def solve(self, root, ret: list):
        if root.left:
            self.solve(root.left, ret)
        if root.right:
            self.solve(root.right, ret)
        if not root.left and not root.right:
            ret.append(root.val)
