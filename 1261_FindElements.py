class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.hashset = set()
        # 此处进行恢复
        root.val = 0
        self.hashset.add(0)
        if root.left:
            self.solve(root.left, 1)
            self.hashset.add(1)
        if root.right:
            self.solve(root.right, 2)
            self.hashset.add(2)

    def find(self, target: int) -> bool:
        # 对类似二叉搜索树式的搜索方式
        return target in self.hashset

    def solve(self, root: TreeNode, x: int):
        root.val = x
        if root.left:
            self.solve(root.left, 2 * x + 1)
            self.hashset.add(root.left.val)
        if root.right:
            self.solve(root.right, 2 * x + 2)
            self.hashset.add(root.right.val)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


if __name__ == "__main__":
    root = TreeNode(-1)
    right = TreeNode(-1)
    root.right = right
    FindElements().find(2)
