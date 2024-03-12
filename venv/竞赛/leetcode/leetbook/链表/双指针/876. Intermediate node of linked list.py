# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/25 9:02'

import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:快慢指针法
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
