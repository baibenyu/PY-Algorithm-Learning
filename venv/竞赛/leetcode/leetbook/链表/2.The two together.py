# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/21 11:39'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:迭代--将链表的结点值相加若超过10则存储具体进位,等待下一个结点的计算,若小于10则直接相加即可,将和赋值给新结点,并连接
    # 实际上就是依次将链表的结点看为数位的个十百千万等,逆序链表更方便进行顺序处理
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dommy = ListNode(-1)
        cur = dommy
        while l1 and l2:
            sum_up = l1.val + l2.val + carry
            cur.next = ListNode(sum_up % 10)
            carry = sum_up // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l2:
            sum_up = l2.val + carry
            cur.next = ListNode(sum_up % 10)
            carry = sum_up // 10
            cur = cur.next
            l2 = l2.next
        while l1:
            sum_up = l1.val + carry
            cur.next = ListNode(sum_up % 10)
            carry = sum_up // 10
            cur = cur.next
            l1 = l1.next
        while carry:
            cur.next = ListNode(carry % 10)
            carry = carry // 10
            cur = cur.next

        return dommy.next
