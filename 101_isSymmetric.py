# 广度优先制作二叉堆,在判断回数序列

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
    def isSymmetric(self, root: TreeNode) -> bool:
        base = [root]
        heap = []

        def isPalindrome(heap):
            size = len(heap)
            _l = 0
            r = size - 1
            while(_l < r):
                if(not heap[_l] or not heap[r]):
                    if(heap[_l] or heap[r]):
                        return False
                elif(heap[_l].val != heap[r].val):
                    return False
                _l += 1
                r -= 1
            return True
        # 转换的操作由循环迭代实现
        while(len(base) == 1 or isPalindrome(base)):
            for node in base:
                if node:
                    heap.append(node.left if node.left else None)
                    heap.append(node.right if node.right else None)
                else:
                    heap.append(None)
                    heap.append(None)
            base = heap
            heap = []
            i = 0
            while(i < len(base)):
                if(base[i] is not None):
                    break
                i += 1
            if(i == len(base)):
                return True
        return isPalindrome(base)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(3)
    Solution().isSymmetric(root)
