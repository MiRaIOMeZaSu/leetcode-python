from typing import List
import queue


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
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # 用栈存储暂时没找到更大值的结点,根据比较出栈并设置值
        ret = []
        stack = []
        curr = head
        index = 0
        while(curr is not None):
            temp = []
            for i in range(len(stack)):
                if stack[i][1] < curr.val:
                    ret[stack[i][0]] = curr.val
                else:
                    temp.append(stack[i])
            stack = temp
            if curr.next is None:
                ret.append(0)
                curr = curr.next
                continue
            if curr.next.val > curr.val:
                ret.append(curr.next.val)
            else:
                stack.append([index, curr.val])
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
    Solution().nextLargerNodes(_1)
