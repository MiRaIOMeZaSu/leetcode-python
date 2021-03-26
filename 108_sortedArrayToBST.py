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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 使用二分
        from math import floor

        def toBST(root, nums, left, right, mid):
            if left > right:
                return
            _mid = floor((left + right) / 2)
            node = TreeNode(nums[_mid])
            if right < mid:
                root.left = node
            else:
                root.right = node
            toBST(node, nums, left, _mid - 1, _mid)
            toBST(node, nums, _mid + 1, right, _mid)
        if len(nums) < 1:
            return
        left = 0
        right = len(nums) - 1
        mid = floor((left + right) / 2)
        root = TreeNode(nums[mid])
        toBST(root, nums, left, mid - 1, mid)
        toBST(root, nums, mid + 1, right, mid)
        return root


if __name__ == "__main__":
    root = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
