"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        arr = []
        copy_arr = []
        while head is not None:
            last = head
            arr.append(last)
            head = head.next
            last.next = Node(last.val)
            copy_arr.append(last.next)
        for node in arr:
            if node.random is None:
                continue
            node.next.random = node.random.next
        for i in range(len(copy_arr) - 1):
            copy_arr[i].next = copy_arr[i + 1]
        return copy_arr[0]