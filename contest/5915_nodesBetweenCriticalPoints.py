from typing import NoReturn, Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans = [-1, -1]
        if head is None:
            return ans

        curr = head.next
        arr = []
        lastVal = head.val
        index = 1
        while curr is not None:
            if curr.next is not None and self.isCriticalPoint(
                    lastVal, curr.val, curr.next.val):
                arr.append(index)
            index += 1
            lastVal = curr.val
            curr = curr.next
        if len(arr) < 2:
            return ans
        ans[-1] = arr[-1] - arr[0]
        ans[0] = float('inf')
        for i in range(1, len(arr)):
            ans[0] = min(arr[i] - arr[i - 1], ans[0])
        return ans

    def isCriticalPoint(self, pres, node, next):
        return (pres > node and node < next) or (pres < node and node > next)
