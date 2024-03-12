# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/16 20:11'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一:利用栈存储链表的逆序遍历,因为回文链表的逆序与顺序都相同,若不同则不是回文链表
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        while stack:
            if stack.pop() != head.val:
                return False
            head = head.next
        return True

    # 方法二:递归,凡是可以用递归实现的代码往往可以用辅助栈+迭代的方法实现,反之同理
    def isPalindrome2(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):  # 递归找到最后一个结点
                    return False
                if self.front_pointer.val != current_node.val:  # 双向比较
                    return False
                self.front_pointer = self.front_pointer.next  # 每比较一次,指针向后移
            return True

        return recursively_check()

    # 方法三:快慢指针+反转链表
    def isPalindrome3(self, head: ListNode) -> bool:
        def reverse_list(head):  # 翻转链表
            previous = None
            current = head
            while current is not None:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous

        def end_of_first_half(head):  # 找链表中点
            fast = head
            slow = head
            while fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            return slow

        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = end_of_first_half(head)
        second_half_start = reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = reverse_list(second_half_start)
        return result
