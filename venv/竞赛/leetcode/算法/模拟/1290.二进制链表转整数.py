# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/30 15:02'

import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:加权相乘
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        ans = 0
        while cur:
            ans = (ans + int(cur.val)) * 2
            cur = cur.next
        return ans // 2
    #

if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
