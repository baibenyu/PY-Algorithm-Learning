# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/27 16:54'

import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:模拟
    # 写之前理清关系,确认需要几个位置变量
    # 本题--1.将k个结点翻转 2.将子链表链回原链表(头连上一个子链表的尾,尾连下一个子链表的头) 3.得到下一个k个结点子链表的开头和结尾
    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:  # 不满k个不翻转
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
