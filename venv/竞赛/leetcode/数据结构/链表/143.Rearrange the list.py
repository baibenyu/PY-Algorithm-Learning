# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/27 17:14'

import time


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:模拟--数组定位+重排
    def reorderList(self, head: ListNode) -> None:
        cur = head
        list1 = list()
        while cur:
            nex = cur.next
            cur.next = None
            list1.append(cur)
            cur = nex
        cur = list1[0]
        i = 1
        left, right = 1, len(list1) - 1
        while left <= right:
            if i:
                cur.next = list1[right]
                right -= 1
            else:
                cur.next = list1[left]
                left += 1
            i = 1 - i
            cur = cur.next


class Solution:
    # 方法二:1.找中点 2.反转后部分链表 3.依次合并两个链表
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
