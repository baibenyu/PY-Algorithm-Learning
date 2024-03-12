# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/20 21:33'

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:迭代法,逐个比较两个链表的结点值,将较小的连接到head结点后
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:  # 四种可能链表组合
            return None
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        else:
            if list1.val < list2.val:  # 确立头结点
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
            cur = head
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            if not list1:  # list1为空但list2不为空,因为本身是升序序列所以只需要连接一次
                cur.next = list2
            if not list2:  # 同上,两个互换
                cur.next = list1
            return head

    # 方法二:递归
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:  # 四种可能链表组合
            return None
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        else:
            if list1.val < list2.val:  # 在递的过程中要确定当前位置应该为两个链表中的哪一个结点,而在归的过程应该将前后结点进行连接,而当前节点
                cur = list1  # 既是上一个结点的后继,也是下一个结点的前驱,要想连接不同递归层中的结点,就必须让函数返回结点
                after = self.mergeTwoLists2(list1.next, list2)
                cur.next = after
            else:
                cur = list2
                after = self.mergeTwoLists2(list1, list2.next)
                cur.next = after
            return cur
