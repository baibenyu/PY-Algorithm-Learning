# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/8 10:06'

import time


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:中序遍历--得到排好序的结点和结点值,然后依次连接
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        list2 = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            list2.append(cur)
            cur = cur.right

        n = len(list2)
        for i in range(n):
            list2[i].left = list2[i - 1]
            list2[i].right = list2[(i + 1) % n]
        return list2[0]

    # 方法二:递归中序遍历
    def treeToDoublyList2(self, root: 'Node') -> 'Node':
        def helper(node):
            nonlocal last, first
            if node:
                helper(node.left)
                if last:  # 连接前后结点
                    last.right = node
                    node.left = last
                else:  # 记录头结点
                    first = node
                last = node
                helper(node.right)

        if not root:
            return None

        first, last = None, None
        helper(root)
        last.right = first
        first.left = last
        return first


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
