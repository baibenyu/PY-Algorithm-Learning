# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/1 16:53'

import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:模拟
    # 环类问题--连接头尾形成环,找到下一个头的位置,并将前驱结点断开
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 0
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        cur.next = head
        n += 1
        k = k % n
        cur = head
        i = 0
        while i != n - k:
            prev = cur
            cur = cur.next
            i += 1
        prev.next = None
        return cur


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
