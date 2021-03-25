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
        self.ret = 0

    def maxDepth(self, root: TreeNode) -> int:
        # DFS

        def dfs(root: TreeNode, depth):
            self.ret = max(depth, self.ret)
            if(root is None):
                return
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)
        return self.ret
