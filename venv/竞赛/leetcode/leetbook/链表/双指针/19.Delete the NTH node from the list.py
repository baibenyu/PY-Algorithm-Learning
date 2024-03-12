# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/21 20:10'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:遍历两遍链表,第一遍确认链表的长度,第二遍找到目标结点并删除
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        cur = head
        position = count - n  # 所给的位置是倒序,转为顺序
        i = 0
        if not position:  # 若是顺序第一个则无前驱结点,直接返回下一个结点即可
            return head.next
        while i < position:
            pre = cur
            cur = cur.next
            i += 1
        cur = cur.next
        pre.next = cur
        return head

    # 方法二:构造辅助栈,根据先入后出的特性,所谓倒数第n个结点即第n个被弹出栈的元素
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)  # 增加一个始终让链表满足总存在前驱结点的哑结点
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next

        for i in range(n):
            stack.pop()

        prev = stack[-1]  # 第n个结点的前驱结点
        prev.next = prev.next.next
        return dummy.next

    # 方法三:双指针法,用指针之间的间隔来指示倒数第n个,当快指针到达末尾时,慢指针与快指针间隔n个结点
    def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy  # 此处为了方便实现删除结点,所以选择让慢指针停在目标结点的前驱结点
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
