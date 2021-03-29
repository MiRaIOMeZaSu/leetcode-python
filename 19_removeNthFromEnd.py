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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 使用快慢指针
        from math import ceil
        slow = head
        fast = head
        length = 1
        pre = None
        while fast:
            fast = fast.next
            if(fast):
                fast = fast.next
                if(not fast):
                    length = length * 2
                    break
            else:
                length = length * 2 - 1
                break
            pre = slow
            slow = slow.next
            length += 1
        # 此时计算出长度
        if n == length:
            return head.next
        index = length - n + 1
        temp = None
        if index > ceil(length / 2):
            # 在之后
            temp = slow
            startIndex = ceil(length / 2)
        elif index == ceil(length / 2):
            pre.next = slow.next
            return head
        else:
            # 在之前
            temp = head
            startIndex = 1

        for i in range(startIndex, index):
            pre = temp
            temp = temp.next
        pre.next = temp.next
        return head


if __name__ == "__main__":
    _1 = ListNode(1)
    _2 = ListNode(2)
    _1.next = _2
    _3 = ListNode(3)
    _2.next = _3
    _4 = ListNode(4)
    _3.next = _4
    _5 = ListNode(5)
    _4.next = _5
    print(Solution().removeNthFromEnd(_1, 4))
