# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/21 23:10'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:  # 当链表结点数小于2时不用排序,返回本身
            return head
        cur = head.next  # 从第二个结点开始进行插入排序
        head.next = None  # 注意!每个结点必须与原链表彻底分离,否则会造成环状链表,死循环
        final = head  # 标记排过序的链表的尾结点,初始为与头结点重合
        while cur:
            if cur.val <= head.val:  # 若小于头结点的值,在前方插入并将头结点向前移
                after = cur.next
                cur.next = head
                head = cur
                cur = after
            elif cur.val >= final.val:  # 若大于尾结点值,在后方插入,并将尾节点向后移
                final.next = cur
                final = cur
                cur = cur.next
                final.next = None
            else:  # 否则遍历排过序的链表,找到比当前待插入结点值大的后继结点,在后继结点前面插入,因为是在链表中间插入,所以要保存前驱结点和后继结点便于插入
                pre = head
                cur2 = head.next
                while cur2.val < cur.val:
                    pre = cur2
                    cur2 = cur2.next
                pre.next = cur
                pre = cur
                cur = cur.next
                pre.next = cur2
        return head
