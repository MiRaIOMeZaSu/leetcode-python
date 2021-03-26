# 使用双指针法

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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        head = headB
        while(headA is not None):
            headB = head
            while(headB is not None):
                if(headA is headB):
                    return headA
                headB = headB.next
            headA = headA.next
        return None
