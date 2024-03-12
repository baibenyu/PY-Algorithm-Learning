# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/21 22:09'
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:自顶向下--归并算法+快慢指针+递归
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
            # 利用快慢指针来指示链表的中点,快指针每次移动两步,慢指针移动一步
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # 分割为两个链表
        # 递归进行分割
        left, right = self.sortList(head), self.sortList(mid)
        # 合并被分割的链表并返回
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right  # 链表长度不同
        return res.next

    # 方法二:自底向上
    def sortList2(self, head: ListNode) -> ListNode:
        # 合并两个链表
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1
        # 根据子链表分割原链表
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                # 定位各子链表及合并
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1

        return dummyHead.next

