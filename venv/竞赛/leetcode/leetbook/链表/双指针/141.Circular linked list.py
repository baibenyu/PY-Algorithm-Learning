# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/21 20:45'

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 方法一:模拟,将已经遍历过的结点存入字典中,判断后序是否还会出现该结点
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        exist = set()
        cur = head
        while cur:
            if cur in exist:
                return True
            exist.add(cur)
            cur = cur.next
        return False

    # 方法二:floyd判圈算法,快慢指针法
    # 如果一个链表不存在环,那么快指针始终在慢指针前方,而不会相遇,若存在环,快指针先进入环中,等慢指针进入后,一定存在某一时刻快指针超过慢指针整圈,也即此时相遇
    def hasCycle2(self, head: ListNode) -> bool:
        if not head or not head.next:  # 少于两个结点无法构成环
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

