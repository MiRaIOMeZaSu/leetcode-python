# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBiNode(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 使用递归
        # 返回头结点
        self.pre = self.ans = TreeNode(-1)

        def convert(root):
            if(not root):
                return None
            # 返回头结点和尾结点组成的元组
            # thisHead = root
            # thisTail = root
            convert(root.left)
            root.left = None
            self.pre.right = root
            self.pre = root
            # lhead, ltail = convert(root.left)
            # ltail.right = root
            # ltail.left = None
            # thisHead = lhead
            convert(root.right)
            # rhead, rtail = convert(root.right)
            # root.right = rhead
            # root.left = None
            # thisTail = rtail
            # return (thisHead, thisTail)
        convert(root)
        return self.ans.right
