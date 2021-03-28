class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        ret = head
        next = 0
        while(l1 or l2):
            val = 0
            if l1 and l2:
                val = l1.val + l2.val + next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val + next
                l1 = l1.next
            elif l2:
                val = l2.val + next
                l2 = l2.next
            # 进行赋值
            head.val = val % 10
            if(val >= 10):
                next = 1
            else:
                next = 0
            if(l1 or l2):
                head.next = ListNode()
                head = head.next
        if(next == 1):
            head.next = ListNode(1)
        return ret
