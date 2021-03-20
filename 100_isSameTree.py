# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 先处理再交给下一次循环
        if(p is None or q is None):
            if(p is None and q is None):
                return True
            return False
        if(p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isSameTree(TreeNode(0), TreeNode(0)))
