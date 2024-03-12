# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/21 12:49'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 方法一:双指针法
    # 逻辑上将两个链表重新组合为A在前B在后和B在前A在后的新链表,此时两个新链表的长度相同,如果两个指针同时开始遍历这两个新链表,那么指针也会同时结束
    # 这两个新链表的重合结点即为原长度不同的链表的重合节点
    # 从结果上看,即实现了长链表指针先移动,而短链表等到长链表缩短到一样长度时才开始移动,保证了指针移动的同步性
    # 或者说实现了两个长度不同的链表的右对齐
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:  # 会在结点重合时或者都为空时结束
            A = A.next if A else headB
            B = B.next if B else headA
        return A

    # 方法二:先移动A指针后移动B指针,并将A和B指针经过的结点存入列表中,在下一次移动前,判断当前A或B指针所指结点是否已经出现过,若出现过则说明该节点即为相交节点
    # 时间和空间复杂度都较高
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        list1 = set()
        while headA or headB:
            if headA:
                list1.add(headA)
                headA = headA.next
            if headB in list1:
                return headB
            if headB:
                list1.add(headB)
                headB = headB.next
            if headA in list1:
                return headA
        return None
