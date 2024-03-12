# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/5 20:48'

import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:哈希表+二次遍历
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dommy = ListNode(-1, head)
        prev = dommy
        cur = head
        seen = set()
        twice = set()
        while cur:  # 删除遇到二次及以上的结点
            if cur.val not in seen:
                seen.add(cur.val)
                cur = cur.next
                prev = prev.next
            else:
                twice.add(cur.val)
                prev.next = cur.next
                cur = cur.next
        cur = dommy.next
        prev = dommy
        while cur:  # 把重复元素删除
            if cur.val in twice:
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
        return dommy.next


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
