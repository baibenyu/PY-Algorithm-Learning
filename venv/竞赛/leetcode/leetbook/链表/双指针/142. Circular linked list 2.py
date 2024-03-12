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
    # 方法一:模拟,将已经遍历过的结点存入字典中,判断后续是否还会出现该结点,且第一次重复即为环的入口
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        exist = set()
        cur = head
        while cur:
            if cur in exist:
                return cur
            exist.add(cur)
            cur = cur.next
        return cur

    # 方法二:floyd判圈算法,快慢指针法
    # 如果一个链表不存在环,那么快指针始终在慢指针前方,而不会相遇,若存在环,快指针先进入环中,等慢指针进入后,一定存在某一时刻快指针超过慢指针整圈,也即此时相遇
    # 注意相遇时并不一定是入口结点,假设快指针的速度是慢指针的两倍,从链表头部到入口距离为a,环长度为b
    # 设快指针经过n圈两个指针相遇,快指针f=2s,f=s+nb->f=2nb,s=nb,若要在入口结点停下,所需的步数为a+kb,如何让慢指针走a步停下?
    # 从快慢指针相遇开始,设置一个新指针从链表头结点开始与慢指针同步运动,当相遇时即经过a步
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
