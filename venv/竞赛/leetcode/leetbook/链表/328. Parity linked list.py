# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/11 9:14'

import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:模拟
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
