# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/28 15:36'

import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:栈
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        else:
            stack = []
            while head:
                stack.append(head)
                head = head.next
            head = stack.pop()
            cur = head
            while stack:
                temp = stack.pop()
                temp.next = None
                cur.next = temp
                cur = cur.next
            return head

    # 方法二:递归
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归终止条件是当前为空，或者下一个节点为空
        if head is None or head.next is None:
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList2(head.next)
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur

    # 方法三:迭代
    def reverseList3(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            nextv = cur.next
            cur.next = pre
            pre = cur
            cur = nextv
        return pre


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
