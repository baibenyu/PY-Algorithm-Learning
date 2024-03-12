# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/5 20:22'

import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:栈+模拟
    def plusOne(self, head: ListNode) -> ListNode:
        cur = head
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next
        carry = 1
        while stack:
            temp = stack.pop()
            temp.val, carry = (temp.val + carry) % 10, (temp.val + carry) // 10
            if not carry:
                break
        if carry:
            new = ListNode(carry, head)
            return new
        return head

    # 方法二:找到最右边不为9的结点+1,
    def plusOne2(self, head: ListNode) -> ListNode:
        # sentinel head
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        # find the rightmost not-nine digit
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

            # increase this rightmost not-nine digit by 1
        not_nine.val += 1
        not_nine = not_nine.next

        # set all the following nines to zeros
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next  # 如果最高位进位则返回现头结点,否则返回原头结点


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
