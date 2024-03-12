# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/22 10:47'

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:选择排序,每次遍历n个链表的头结点,将最小的结点加入结果链表,并将该链表的指针后移
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        dummyhead = ListNode(0)
        cur = dummyhead
        while True:
            flag = False
            minnum = float("inf")
            index = 0
            for i in range(length):
                if lists[i]:
                    if lists[i].val < minnum:
                        minnum = lists[i].val
                        index = i
                        flag = True
            if flag:
                cur.next = lists[index]
                cur = cur.next
                lists[index] = lists[index].next
                cur.next = None
            else:
                return dummyhead.next

    # 方法二:归并排序+合并链表
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        n = len(lists)  # 记录子链表数量
        return self.mergeSort(lists, 0, n - 1)  # 调用归并排序函数

    def mergeSort(self, lists: List[ListNode], l: int, r: int) -> ListNode:
        if l == r:
            return lists[l]
        m = (l + r) // 2
        L = self.mergeSort(lists, l, m)  # 循环的递归部分
        R = self.mergeSort(lists, m + 1, r)
        return self.mergeTwoLists(L, R)  # 调用两链表合并函数

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # 构造虚节点
        move = dummy  # 设置移动节点等于虚节点
        while l1 and l2:  # 都不空时
            if l1.val < l2.val:
                move.next = l1  # 移动节点指向数小的链表
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2  # 连接后续非空链表
        return dummy.next  # 虚节点仍在开头

    # 方法三:构造小根堆,并每次将堆的头结点连接到新链表中
    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        import heapq  # 调用python标准库自带的小根堆
        minHeap = []
        for listi in lists:
            while listi:
                heapq.heappush(minHeap, listi.val)  # 把listi中的数据逐个加到小根堆中,python的堆结构会自动维护自身
                listi = listi.next
        dummy = ListNode(0)  # 构造虚节点
        p = dummy
        while minHeap:
            p.next = ListNode(heapq.heappop(minHeap))  # 依次弹出小根堆头结点的数据
            p = p.next
        return dummy.next
