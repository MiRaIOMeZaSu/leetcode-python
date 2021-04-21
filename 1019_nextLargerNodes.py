from typing import List
import queue
from sortedcontainers import SortedList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyItem:
    def __init__(self, index, val):
        self.index = index
        self.val = val

    def __lt__(self, o):
        return self.val < o.val

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # 用栈存储暂时没找到更大值的结点,根据比较出栈并设置值
        ret = []
        stack = SortedList()
        curr = head
        index = 0
        while(curr is not None):
            while(len(stack) > 0):
                if stack[0].val < curr.val:
                    ret[stack[0].index] = curr.val
                    stack.pop(0)
                else:
                    break
            if curr.next is None:
                ret.append(0)
                curr = curr.next
                continue
            if curr.next.val > curr.val:
                ret.append(curr.next.val)
            else:
                stack.add(MyItem(index, curr.val))
                ret.append(0)
            curr = curr.next
            index += 1
        return ret


if __name__ == "__main__":
    _1 = ListNode(2)
    _2 = ListNode(1)
    _3 = ListNode(5)
    _1.next = _2
    _2.next = _3
    print(Solution().nextLargerNodes(_1))
