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
        self.d = dict()
        self.sum = 0
        self.ret = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.sum = sum
        if(root is not None):
            self.solve(root)
        return self.ret

    def solve(self, root: TreeNode):
        # 保证不会有空输入
        num = self.sum - root.val
        if(num == 0):
            self.ret += 1
        if(num in self.d):
            self.ret += self.d[num]
        if(root.left or root.right):
            temp = {}
            for key in self.d.keys():
                temp[key + root.val] = self.d[key]
            temp[root.val] = 1 if root.val not in temp else temp[root.val] + 1
            self.d = temp

            def remove(_val):
                temp = dict()
                if(self.d[_val] > 1):
                    self.d[_val] -= 1
                else:
                    self.d.pop(_val)
                for key in self.d.keys():
                    temp[key - _val] = self.d[key]
                self.d = temp

            if(root.left):
                val = root.left.val
                if(self.solve(root.left)):
                    remove(val)
            if(root.right):
                val = root.right.val
                if(self.solve(root.right)):
                    remove(val)
            return True
        return False


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

# _1 = TreeNode(10)
# _2 = TreeNode(5)
# _3 = TreeNode(-3)
# _4 = TreeNode(3)
# _5 = TreeNode(2)
# _6 = TreeNode(11)
# _7 = TreeNode(3)
# _8 = TreeNode(-2)
# _9 = TreeNode(1)
# _1.left = _2
# _1.right = _3
# _2.left = _4
# _2.right = _5
# _3.right = _6
# _4.left = _7
# _4.right = _8
# _5.right = _9
_1 = TreeNode(0)
solution = Solution()
solution.pathSum(_1, 0)
