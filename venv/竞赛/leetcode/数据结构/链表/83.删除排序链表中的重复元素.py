# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/28 15:49'

import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        else:
            prev = head
            cur = prev.next
            while cur:
                while cur and prev.val == cur.val:
                    cur = cur.next
                prev.next = cur
                prev = cur
                if cur:
                    cur = cur.next
            return head


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
