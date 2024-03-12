# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/19 14:54'

import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:递归
    def dfs(self, head: ListNode, rt: TreeNode) -> bool:
        if not head:  # 若链表匹配到None说明都匹配完了,返回True
            return True
        if not rt:  # 若树结点为空则不可能与链表的值匹配直接返回False
            return False
        if rt.val != head.val:  # 值不同
            return False
        return self.dfs(head.next, rt.left) or self.dfs(head.next, rt.right)

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right) # 尝试树上的所有结点作为起始结点


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
