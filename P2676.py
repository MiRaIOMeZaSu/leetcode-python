# 使用链表
class ListNode():
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val
# 使用插值排序


def insert(listnode: ListNode, i: int):
    # 进行插入(保持序列递增)
    head = listnode
    now = listnode.next
    if(now is None):
        listnode.next = ListNode(i)
        return
    while(now is not None):
        if(now.val >= i):
            _new = ListNode(i)
            head.next = _new
            _new.next = now
            return
        head = now
        now = now.next
    _new = ListNode(i)
    head.next = _new


info = [int(i) for i in input().split()]

# 用于标记链表的头
Vhead = ListNode(-1)
a = int(input())
head = ListNode(a)
Vhead.next = head
sum = a
size = 1
for i in range(info[0] - 1):
    a = int(input())
    if(sum > info[1]):
        if(a > Vhead.next.val):
            # 此时进行判断更新操作
            sum += a
            insert(Vhead, a)
            size += 1
            while(sum - Vhead.next.val > info[1]):
                sum -= Vhead.next.val
                Vhead.next = Vhead.next.next
                size -= 1
        continue
    insert(Vhead, a)
    size += 1
    sum += a
print(size)
