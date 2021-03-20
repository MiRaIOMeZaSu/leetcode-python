# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeGener(object):
    def genTree(self, arr):
        def gen(arr, i):
            if i < len(arr):
                tn = TreeNode(arr[i]) if arr[i] is not None else None
                if tn is not None:
                    tn.left = gen(arr, 2 * i + 1)
                    tn.right = gen(arr, 2 * i + 2)
                return tn
        return gen(arr, 0)


class Solution(object):
    def convertBiNode(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 使用递归
        # 返回头结点
        if(root is None):
            return None
        rhead, lhead = None, None
        if(root.left is not None):
            lhead, ltail = self.convert(root.left)
            ltail.right = root
        if(root.right is not None):
            rhead, rtail = self.convert(root.right)

        root.left = None
        root.right = rhead
        return lhead if lhead is not None else root

    def convert(self, root):
        # 返回头结点和尾结点组成的元组
        thisHead = root
        thisTail = root
        if(root is None):
            return (None, None)
        if(root.left is not None):
            lhead, ltail = self.convert(root.left)
            ltail.right = root
            ltail.left = None
            thisHead = lhead
        if(root.right is not None):
            rhead, rtail = self.convert(root.right)
            root.right = rhead
            root.left = None
            thisTail = rtail
        return (thisHead, thisTail)


if __name__ == "__main__":
    root = TreeGener().genTree([4, 2, 5, 1, 3, None, 6, 0])
    result = Solution().convertBiNode(root)
    print("结束")
