# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(not l1 or not l2):
            # 任意一个链为空时直接返回
            return l2 if not l1 else l1
        self.head = l1 if l1.val <= l2.val else l2
        while(l1):
            if(l1.val > l2.val):
                temp = l1
                l1 = l2
                l2 = temp
            else:
                # 此时l1值必定小于等于l2
                if l1.next:
                    if l1.next.val >= l2.val:
                        _next = l1.next
                        l1.next = l2
                        now = l2.next
                        preNow = l2
                        while now and now.val <= _next.val:
                            preNow = now
                            now = now.next
                        preNow.next = _next
                        if now:
                            l2 = now
                            l1 = _next
                        else:
                            return self.head
                    else:
                        l1 = l1.next
                else:
                    l1.next = l2
                    return self.head


if __name__ == "__main__":
    l1 = ListNode(1)
    _2 = ListNode(2)
    l1.next = _2
    _3 = ListNode(4)
    _2.next = _3
    l2 = ListNode(1)
    _2 = ListNode(2)
    l2.next = _2
    _3 = ListNode(4)
    _2.next = _3
    Solution().mergeTwoLists(l1, l2)
