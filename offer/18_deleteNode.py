

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
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 只删除一次
        if head is None:
            return None
        if head.val == val:
            return head.next
        last = head
        curr = last.next
        while curr is not None:
            if curr.val == val:
                last.next = curr.next
                return head
            last = curr
            curr = last.next
        return head


if __name__ == "__main__":
    _1 = ListNode(4)
    _2 = ListNode(5)
    _1.next = _2
    _3 = ListNode(1)
    _2.next = _3
    _4 = ListNode(5)
    _3.next = _4
    _5 = ListNode(9)
    _4.next = _5
    Solution().deleteNode(_1, 5)
