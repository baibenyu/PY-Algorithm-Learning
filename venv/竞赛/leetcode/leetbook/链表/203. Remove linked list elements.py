# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 20:39'

import time


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:迭代,指针的变换
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        headv = ListNode(-1, head)
        prev = headv
        cur = prev.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return headv.next

    # 方法二:递归
    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        else:
            head.next = self.removeElements2(head.next, val)
            return head if head.val != val else head.next


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
