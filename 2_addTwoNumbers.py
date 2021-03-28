class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)  # 保存头结点，返回结果
        s = 0  # 每一步的求和暂存变量
        while l1 or l2 or s:  # 循环条件：l1 或者l2（没有遍历完成），s(进位)不为0
            # 这其实是好多代码，我自己写了好多行，但是作者这样写非常简洁，赞
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)  # 构建新的list存储结果，其实用较长的加数链表存也可以，%10：求个位
            p = p.next
            s //= 10  # 求进位
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # 重要的步骤: 忽视开头用于方便适应第一次循环和之后循环的区别
        return dummy.next
