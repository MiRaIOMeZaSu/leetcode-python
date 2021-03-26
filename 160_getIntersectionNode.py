# 使用双指针法
# 对每个结点尽心比较的时间复杂度为n!,将导致超时
# 只判断尾结点则无法获取交点
# 首先使用快慢指针分辨获取长度,再根据差值同时后移指针获取交点
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
        def getLen(head):
            slow = head
            fast = head
            i = 1
            while(fast.next is not None and fast.next.next is not None):
                slow = slow.next
                fast = fast.next.next
                i += 2
            if(fast.next is not None):
                i += 1
                last = fast.next
            else:
                last = fast
            return i, last
        lenA, lastA = getLen(headA)
        lenB, lastB = getLen(headB)
        if(lastA is not lastB):
            return None
        longer = headA
        shorter = headB
        longLen = lenA
        shortLen = lenB
        if lenA < lenB:
            longer = headB
            shorter = headA
            longLen = lenB
            shortLen = lenA
        sub = longLen - shortLen
        for i in range(0, sub):
            longer = longer.next
        while(shorter is not longer):
            longer = longer.next
            shorter = shorter.next
        return shorter
