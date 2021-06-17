from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        ret = []
        curr = head
        while curr is not None:
            stack.append(curr)
            curr = curr.next
        while len(stack) != 0:
            ret.append(stack[-1].val)
            stack.pop()
        return ret
