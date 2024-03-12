# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/1 16:36'

import time


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:取出链表中的数字相加后,再按位生成新链表,但位数可能过大>64位,在一些其它语言中要用数组或者字符串存储
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = 0
        if l1.val == 0 and l2.val == 0:
            return ListNode()
        while l1:
            n1 = n1 * 10 + l1.val
            l1 = l1.next
        n2 = 0
        while l2:
            n2 = n2 * 10 + l2.val
            l2 = l2.next
        ans = n1 + n2
        stack = []
        while ans:
            stack.append(ans % 10)
            ans = ans // 10
        dommy = ListNode(-1)
        cur = dommy
        for i in range(len(stack) - 1, -1, -1):
            cur.next = ListNode(stack[i])
            cur = cur.next
        return dommy.next

    # 方法二:栈
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
