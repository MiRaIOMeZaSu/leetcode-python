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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.root = None
        self.last = None
        if root:
            self.solve(root)
        return self.root

    def solve(self, node):
        if(node.left):
            self.solve(node.left)
        if not self.root:
            self.root = node
        if self.last:
            self.last.right = node
        self.last = node
        self.last.left = None
        if(node.right):
            self.solve(node.right)


if __name__ == "__main__":
    '''
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
        10
        /  \
       5   -3
      / \    \
      3   2   11
    / \   \
   3  -2   1
    '''
    _1 = TreeNode(5)
    _2 = TreeNode(3)
    _3 = TreeNode(6)
    _4 = TreeNode(2)
    _5 = TreeNode(4)
    _6 = TreeNode(1)
    _7 = TreeNode(3)
    _8 = TreeNode(8)
    _9 = TreeNode(7)
    _10 = TreeNode(9)
    _1.left = _2
    _1.right = _3
    _2.left = _4
    _2.right = _5
    _4.left = _6
    _3.right = _8
    _8.left = _9
    _8.right = _10
    Solution().increasingBST(_1)
